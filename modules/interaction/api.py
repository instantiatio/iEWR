"""I invokes C, presents material outcome and retains a complete text fallback."""
from typing import Protocol
from modules.coordination.api import (Coordination, Binding, EditBasis, ActionScope,
                                      Observation, Receipt, UseAssessment, OperationBasis,
                                      Question, AnswerDraft, Use)

# Transport re-exports preserve the producer's identity; no shared semantic type.
INPUT_VALUES = {cls.__name__: cls for cls in
                (Binding, EditBasis, ActionScope, Observation, Receipt, UseAssessment, OperationBasis,
                 Question, AnswerDraft, Use)}


class Renderer(Protocol):
    def render(self, text: str) -> str: ...


class Interaction:
    def __init__(self, coordination: Coordination, renderer: Renderer):
        self.coordination, self.renderer = coordination, renderer

    def submit(self, owner: str, operation: str, **values):
        return self.coordination.dispatch(owner, operation, **values)

    def capture_response(self, text, interpretations=()):
        # This is a draft only; the direct channel and G retain authoritative evidence.
        if any(d.exact_span not in text for d in interpretations):
            raise ValueError("interpretation_span_not_in_received_text")
        return {"text": text, "drafts": tuple(interpretations), "limit": "requires_G_direct_source_assessment"}

    def present(self, target: str, outcome: str, reason: str) -> str:
        if outcome == "done":
            text = f"Исправлено: {target}. Конечный текст проверен."
        elif outcome == "reuse":
            text = f"В {target} уже находится нужный текст. Повторная правка не требуется."
        else:
            # Exact machine reason retained for audit, ordinary text groups its meaning.
            if any(word in reason for word in ("unresolved", "storage", "pending", "replay")):
                detail = "Итог предыдущего действия или его учёт не установлен. Повторное выполнение удерживается."
            elif any(word in reason for word in ("decision", "permission", "authority", "condition")):
                detail = "Нет достаточного текущего основания для этой правки; проверьте предмет, срок и условия разрешения."
            elif any(word in reason for word in ("path", "unsafe", "control", "symlink")):
                detail = "Не подтверждена необходимая техническая граница записи."
            else:
                detail = "Исходный текст или необходимая основа изменились; зависимое действие остановлено."
            text = f"Правка {target} не завершена. {detail}"
        try:
            rendered = self.renderer.render(text)
            # Renderer is optional. It may decorate, but cannot remove any material text.
            return rendered if text in rendered else text
        except Exception:
            return text
