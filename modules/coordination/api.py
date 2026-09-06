"""C dispatches exactly one explicit owner call. No stages, queue, loop, or scheduler."""
from modules.sources.api import Binding, inspect_binding
from modules.governance.api import Governance, ActionScope
from modules.effects.api import Effects, Observation, Receipt
from modules.reliance.api import assess_use, UseAssessment
from modules.formation.api import EditBasis, form_next_result_basis
from modules.execution.api import Execution
from modules.sources.repertoire import SourceResolution
from modules.governance.operations import OperationGovernance
from modules.effects.operations import OperationEffects
from modules.execution.operations import OperationExecution
from modules.recovery.api import Recovery, discover, impact
from modules.formation.execution_basis import plan_need, readiness_use, external_contribution
from modules.execution.work_basis import assess_work_basis
from modules.governance.responses import DecisionResponses, Question, AnswerDraft
from modules.reliance.assessment import Use, assess, RelianceRecords
from modules.formation.operations import OperationBasis


class Coordination:
    def __init__(self, source_reader, governance_reader, clock, actuator, effect_store, execution_store):
        # Static construction of public owners, no observation or actuation here.
        self.sources = source_reader
        self.governance = Governance(governance_reader, clock)
        self.effects = Effects(self.governance, actuator, effect_store)
        self.execution = Execution(self.governance, self.effects, execution_store)

    def attach_operations(self, source_reader, decision_reader, clock, actuator, effect_store, execution_store):
        self.source_resolution = SourceResolution(source_reader)
        self.operation_governance = OperationGovernance(decision_reader, clock)
        self.operation_effects = OperationEffects(self.operation_governance, actuator, effect_store)
        self.operation_execution = OperationExecution(self.operation_governance, self.operation_effects, execution_store)

    def attach_recovery(self, governance_query, basis_query, facts_query):
        self.recovery = Recovery(governance_query, basis_query, facts_query)

    def attach_decisions(self, response_source, governance_store, reliance_store, clock):
        self.responses = DecisionResponses(response_source, governance_store, clock)
        self.reliance_records = RelianceRecords(reliance_store)

    def dispatch(self, owner: str, operation: str, **values):
        calls = {
            ("S", "inspect_binding"): lambda: inspect_binding(self.sources, **values),
            ("F", "form_next_result_basis"): lambda: form_next_result_basis(**values),
            ("G", "resolve_relations"): lambda: self.governance.resolve_relations(**values),
            ("E", "observe_effect"): lambda: self.effects.observe_effect(**values),
            ("E", "assess_boundary"): self.effects.assess_boundary,
            ("X", "attempt_action"): lambda: self.execution.attempt_action(**values),
            ("X", "read_execution"): lambda: self.execution.read_execution(**values),
            ("L", "assess_use"): lambda: assess_use(**values),
            ("F", "plan_need"): lambda: plan_need(**values),
            ("F", "readiness_use"): lambda: readiness_use(**values),
            ("F", "external_contribution"): lambda: external_contribution(**values),
            ("X", "assess_work_basis"): lambda: assess_work_basis(**values),
            ("R", "discover"): lambda: discover(**values),
            ("R", "impact"): lambda: impact(**values),
            ("R", "select_successor"): lambda: Recovery.select_successor(**values),
            ("L", "assess_receiving_use"): lambda: assess(**values),
        }
        call = calls.get((owner, operation))
        if call is None and (owner, operation) == ("R", "reconstruct") and hasattr(self, "recovery"):
            call = lambda: self.recovery.reconstruct(**values)
        if call is None and hasattr(self, "responses"):
            selected = {("G", "assess_response"): self.responses.assess,
                        ("G", "response_records"): self.responses.records,
                        ("L", "observe_reliance"): self.reliance_records.observe_reliance}.get((owner, operation))
            if selected:
                call = lambda: selected(**values)
        if call is None and hasattr(self, "source_resolution"):
            additions = {
                ("S", "inspect_source"): self.source_resolution.inspect,
                ("S", "candidates"): self.source_resolution.candidates,
                ("S", "verify_source"): self.source_resolution.verify,
                ("S", "contribute"): self.source_resolution.contribute,
                ("X", "attempt_operation"): self.operation_execution.attempt,
                ("X", "operation_records"): self.operation_execution.records,
                ("E", "operation_records"): self.operation_effects.records,
            }
            selected = additions.get((owner, operation))
            if selected:
                call = lambda: selected(**values)
        if call is None:
            raise ValueError("unsupported_explicit_owner_operation")
        return call()
