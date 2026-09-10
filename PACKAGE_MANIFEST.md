# iEWR 5.2.2-beta.3 — состав основной ветки, сведения о публикации 1

| Параметр | Значение |
|---|---|
| Идентификатор текущей редакции | `iEWR-5.2.2-beta.3-publication.1` |
| Программная версия | `5.2.2-beta.3` |
| Редакция сведений о публикации | 1 |
| Статус | Принятая редакция документации 2 опубликована; здесь отдельно обновлены сведения о выпуске |
| Принятая исходная поставка | `iEWR-5.2.2-beta.3-docs.2`, 100 файлов |
| SHA-256 исходного ZIP | `07df4f29c635c2807aec80f28d9c34ac36e4dd68ae2c95b3e9f6a8b67ee61bdd` |
| Первоначальная основа | Предоставленная пользователем `iEWR-5.2.1-beta`; приёмка из предоставления не выводится |
| Архитектура | Контракт ядра 1.0 RC; код, интерфейсы и зависимости модулей сохранены |
| DPF | Авторская дата 2026-09-05; закреплённая редакция `2026-09-05-rev-d514a6fc` сохранена |
| distribution_ready | `false` |
| Публичная публикация | [Принятый архив без пересборки](https://github.com/instantiatio/iEWR/releases/tag/v5.2.2-beta.3) |

Изменения и ограничения: [сведения о поставке](BASELINE_STATUS.md).
Лицензии: [уведомление об источниках](frameworks/dpf/NOTICE.md), [лицензия iEWR](LICENSE).
Авторство производных справочных материалов сохранено в [каталоге DPF](catalog/dpf/README.md).
Локальный SDLC остаётся экспериментальным материалом; ядро и источники не обновлялись.

Продукт ограничен перечисленными файлами. Пользовательские материалы, результаты,
история, испытательные копии и вспомогательные средства разработки исключены.
Структура проекта в пакете — README и пустые маркеры source/handoff/artifacts.
Прежний reference не переносится и не удаляется. Собственная контрольная сумма
этой ведомости указана в сопровождающем отчёте.

## Точный состав

100 файлов: 99 строк контрольных сумм и 98 файлов в описании конфигурации.

| Путь | Назначение | SHA-256 |
|---|---|---|
| `AGENTS.md` | Файл поставки | 2fbcb3d98477cc8e6f8239f73e6ce128ec0998f718ff35ab46873806d0ba6fb2 |
| `BASELINE_STATUS.md` | Файл поставки | 68d77a6133f11efccf1e9f8b2ee1e609b7bb360d4781fdf30216a99dfea72042 |
| `ENGINEERING_WORK_BOOTSTRAP_GUIDE.md` | Файл поставки | b765f4d1167471a63dc70e0045427a380442f1081d50e3837973296eb2616dab |
| `LICENSE` | Файл поставки | ef4da070e506cd1018f449fc78bae57537b96f797264cf56f133e411b5b611ec |
| `MODEL_SELECTION_RECOMMENDATIONS.md` | Файл поставки | b7059b78fd8a6d90e677520fbaf880ce6ef0634855e597d56847f590fec43490 |
| `README.md` | Файл поставки | edd4d347bac7395b5426dc2dc06b1d4d673ec5d46b9814db1aef498698befdcd |
| `WORKING_PROCESS_AND_LOOPS_GUIDE.md` | Файл поставки | 60f642ae1eb19a05669a7f0c86e6ba65a0e47f186718df41c85cf6fce097f557 |
| `adapters/ADAPTERS.md` | Файл поставки | 17a6463da3068d39b7f84074308c1481a512e6e44e83e2faaaedd30b67765d86 |
| `adapters/agent_host/channel.py` | Файл поставки | 115d747d2dbb037cf2e6f1a912ccb939d5c347343eb47d92db8e751a478f0390 |
| `adapters/agent_host/responses.py` | Файл поставки | 6dc5ca67a3f081248c6717e512dc87b87d3f7f2dd6cb0a997354fad2889323dd |
| `adapters/filesystem/artifacts.py` | Файл поставки | f5309420636b03486c62232d5ed1e7d19239a39fc567bfb2776cb1fe9261ae20 |
| `adapters/filesystem/local.py` | Файл поставки | 5f0bd1dde5f6e3d8ea44609b6c6d53c9e57ae93838e3ba7b664e79893f22a0c0 |
| `adapters/filesystem/recovery.py` | Файл поставки | 9112729bb1f4b7abd219f9f4d0a77300ac6ae3986c8593b8e379625d92a31ba6 |
| `adapters/filesystem/repertoire.py` | Файл поставки | 025559c5cfcccf766c37bd4b198dbff21d7ce6d558780fa6c6636f43a50b5d43 |
| `adapters/filesystem/repertoire_engine.py` | Файл поставки | 21bdde5b57e80544b49ea588ca246099955afcd71b9525bc3135a0652ece53fd |
| `adapters/presentation/text.py` | Файл поставки | 84442e0aa5a586610717f5f66dce9e91cc37d7e8969f2f8bfa9876b386d41415 |
| `app/bootstrap/CONFIGURATION.json` | Файл поставки | 1b2c817f0bab5e345d24375b00134d2b481c47a35edd68b339cd15ce0f5270e1 |
| `app/bootstrap/ENTRY.md` | Файл поставки | 5f9851ed231c3235176c4e9efc03d254d19b8d71e0284c7502b18137d2a1e224 |
| `app/bootstrap/operation.py` | Файл поставки | 6fde3ea71cfcb8c9039c711713e60116bf56c9316370b50d91a61a9c056a0d5f |
| `catalog/README.md` | Файл поставки | 85a82976fc5b058a95c08627a5533854a83072aafe973e50b2344260e866cd85 |
| `catalog/dpf/CARDS.md` | Файл поставки | d24bd253beadc09c65330a0b3bf25f8671b4f663bd51d8351b7a656009795909 |
| `catalog/dpf/CARD_TEMPLATE.md` | Файл поставки | d3175088a6a4694cb946b5c490d856a7e4c1e57840342a2ad3513cb39f807e85 |
| `catalog/dpf/GUIDE.md` | Файл поставки | c76d3edc9ed59c17ee96f3579897360c9d7b8df4cbae775146e057b425b661d1 |
| `catalog/dpf/README.md` | Файл поставки | 6d4031ce59ff5fc53674e7a13a5109d09398fc0a8235969c86b3b94b7fbe39bb |
| `catalog/engineering_views/CATALOG.md` | Файл поставки | 04362cc56908a077c47d206a9064501c8285341e6285f38352a0760db5a5ae34 |
| `catalog/engineering_views/README.md` | Файл поставки | 0576c71190c4eac933529532d9a1ca9e91a435593ca50b1117f0e6f881099c00 |
| `catalog/engineering_views/templates/PROJECT_VIEW_PROFILE.yaml` | Файл поставки | 96a70940fa3a6d1aa0130481337ada9b05573923f2797f7e9ff6dc2ae2b970b6 |
| `catalog/working_process_compositions/CATALOG.md` | Файл поставки | 35618f6dc9c84bf782321daa6ab8e12794f4f3cb4a9c2d9102cd75757596c472 |
| `catalog/working_process_compositions/README.md` | Файл поставки | 6e2585504014ba917c4acf7b39bd5c104fcb203a841f50b2e4805d5db2b4ce76 |
| `catalog/working_process_compositions/templates/WORKING_PROCESS_COMPOSITION_RECORD.yaml` | Файл поставки | 4ae37efc59297fc6d2700799ef484143f825c7c8e4c6a7b2f6879c9da3bdd449 |
| `docs/BUNDLED_DPF_BASELINE_REFRESH_AND_INTEGRATION_GUIDE.md` | Файл поставки | 610573e28fb9bfa55b26196622a27bf00aab4d5a885b0fa06b900fee17314114 |
| `docs/DPF_FORMATION_METHOD.md` | Файл поставки | f5720bc446534877da42fa63b5c7c30de7e38110e8c7bbd17839735450bd8b52 |
| `docs/DPF_REGISTRATION_GUIDE.md` | Файл поставки | a1e59bfc96b431cd4a5b5d829029844c2d2eed6281fe5444130d59eb25661dc2 |
| `docs/EWR_CORE_ARCHITECTURE_CONTRACT.md` | Файл поставки | ea9842606c82af26b3217fae8d743e99e0030ec56ce089b69ad25c551b65343c |
| `frameworks/dpf/LICENSE` | Файл поставки | 9e5f1b3c610b9c2da5c313bf81d577a7d1acec686bdb0384edefa6df0f90cd94 |
| `frameworks/dpf/LICENSING.md` | Файл поставки | f80502802237f19a0ea85303a792281e0f9c533e86d23f8a6174d5c18bd70864 |
| `frameworks/dpf/NOTICE.md` | Файл поставки | 17a0eafe4c07c5a5f7d15f0682dc067071cd6660f738a2c26b4ae010602e9b6e |
| `frameworks/dpf/REPERTOIRE.yaml` | Файл поставки | f7ebd9be7a1d1d575fa6243c5b03fcb36e5e47dc59e529036b91d5d9bcee384c |
| `frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | Файл поставки | cc9056e958c0435ec33666291f6fa4bb207d5e307ae6b28213f134f74d92bef4 |
| `frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md` | Файл поставки | 5d2ff495c0a6fff809092c8e36c826ae3a6d94860cf58d63ef61a41feaeedd87 |
| `frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | Файл поставки | a7ab62df62afe22086165830d0c91bf04c43d07437431f7d6944c571894da5ac |
| `frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md` | Файл поставки | dbf0f86337d24dcb89d90faa38240991579b9fe6d1487120285c36126673efa9 |
| `frameworks/dpf/sdlc/0.1.0/SDLC_DPF.md` | Файл поставки | eb6e5b1e69ee8192fbcd73acf05bca3484ac2637f79abb810e63d06e3a25f7da |
| `frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | Файл поставки | 45c49096102c11c7ac1024e3b459f7b9e791c48613163af46f2d63cfdf579887 |
| `modules/coordination/CONTRACT.md` | Файл поставки | 66a8cad0e6839587d48025c8e0840ff83c37e1d6a7638f40bd0e034e9bcaeebd |
| `modules/coordination/GUIDANCE.md` | Файл поставки | 5fc0479d7787ca8d09242c529c78f0c62f16b15cfb87c7d13c8a34895c4fae54 |
| `modules/coordination/api.py` | Файл поставки | 2df8fb261287a54744cfa92cbb9c958bc96114bdc2fa564a0d32999a6ee735ea |
| `modules/effects/CONTRACT.md` | Файл поставки | 38339720cde001c4af4af3eac242af2e8395f13dd2d7a156efc14644c4c8f44b |
| `modules/effects/GUIDANCE.md` | Файл поставки | 6aef670f0a9c303e69a97f0afa03a4d83e3ed66bf4cea5ddf51a8eef31e55cde |
| `modules/effects/api.py` | Файл поставки | 054142aaea6287187238cf97dcd1f9d3a852224d77360b6daa907a375155a3bf |
| `modules/effects/operations.py` | Файл поставки | ec2be5ef2b71b9836772ffc935a95724104e8b7f63ce2f5511035efd6ee699f6 |
| `modules/execution/CONTRACT.md` | Файл поставки | 1aabccabf4a4674080dce494918920466ebb4d14fe3fde14d3758405a0f09cee |
| `modules/execution/EXECUTION_BASIS.md` | Файл поставки | f0393305bd84bd8f103ef48091dffd975bc1616a60b267981949488165f37020 |
| `modules/execution/api.py` | Файл поставки | 5f50847385764a116a0042465926b9ba5cfe45938d8de68a3bb680ec89ccc9b0 |
| `modules/execution/operations.py` | Файл поставки | af38d55cf76b4472977fa6d7369bfac6358e019cd6a0fc8155254123db7bd66e |
| `modules/execution/profiles.py` | Файл поставки | ee01627ed36b5543c5b8402602b1d372b32e5e71ea91b584918095b660ad9f92 |
| `modules/execution/work_basis.py` | Файл поставки | d96f29cf52f4474b99b572daa29be14e2367f0b5045c7fe0cb68dd0a4428e16b |
| `modules/formation/CONTRACT.md` | Файл поставки | 604d41cb8c9b80d299830f276411a02cc1f00ee441a67eaa5159451b41870ba8 |
| `modules/formation/DOMAIN_WORK.md` | Файл поставки | b94fc73d9985b0781fa4c166cb1580bbb1a1dff1d971599a4fd6f5a36558ac76 |
| `modules/formation/api.py` | Файл поставки | c2ffb6dd62fa3fec34b6e06fb5ce369091653ea26778965b6ad342788f8f2bc1 |
| `modules/formation/execution_basis.py` | Файл поставки | 01b3ac1d646126ed42f13a7b21878f597603b7986a0959f89279056d8ad60440 |
| `modules/formation/operations.py` | Файл поставки | 2d32a3f45424d43e3fd29e8a217c10b882150ad23d11860a3ec42d8d27279573 |
| `modules/governance/CONTRACT.md` | Файл поставки | 93a666400239dcf6b9ccbcb8855032fc93e3ae5899ebc232a331461c87acf5b3 |
| `modules/governance/GUIDANCE.md` | Файл поставки | e25d69529e019929f49c059dee2514d63e2d965c1f2a423827192cb8a268b891 |
| `modules/governance/api.py` | Файл поставки | aa7fa47660da19204449452102ec8586a87ea1ab08b9e17514f8ea47815ca6ca |
| `modules/governance/operations.py` | Файл поставки | 8a28acc269b1c6ea82b86b990fd9560e7b2574a728643435b15d3c32e302927e |
| `modules/governance/responses.py` | Файл поставки | 11fc582eb81eb3d1df75c16b626c4e46b4da500c2375bd1626906a5b8680cd0c |
| `modules/interaction/CONTRACT.md` | Файл поставки | d149e12fd6a373551d09a9620933b8b5a40ecd555c89e4024cc72406dca19439 |
| `modules/interaction/HUMAN_INTERACTION.md` | Файл поставки | 865932f8895f069bca816c471a265cbb2412b06efcb17ea6e9762141cece0059 |
| `modules/interaction/api.py` | Файл поставки | 57c2ef8e1926c0f37a0c158b5eebef315c060b6aad94726eb7f3209fbd56a5a0 |
| `modules/interaction/preferences.py` | Файл поставки | de98c54aa3652bb5518442a6f8c174dfce7c8c3c0ccbd66c0b7f80eeb7356d99 |
| `modules/interaction/presentation.py` | Файл поставки | c4749c9cac50683383d29cbf85bd03339a32ea164ea5b901273d97398edadd49 |
| `modules/recovery/CONTRACT.md` | Файл поставки | 83db9a9dc18e175d93276b07f518c593db89986e019458698d64d65535ee41e2 |
| `modules/recovery/api.py` | Файл поставки | 12cb724d22c89207fcf7fb183f3860a911fba8e7d8c06f01c6f072601ab755e5 |
| `modules/reliance/CONTRACT.md` | Файл поставки | 7458f8dd2d291a510ec20520dc454d890d80da0aae62b379bdaa5e74f2c42674 |
| `modules/reliance/RECEIVING_USE.md` | Файл поставки | d6f6fc745d52a1705774bb40efb2890286c0d4b74ed1c6ceefe8d05baf89ffd3 |
| `modules/reliance/api.py` | Файл поставки | fc0b842468dc11dd5f5bb2ee902697e62294699de097354010602d95370d28a9 |
| `modules/reliance/assessment.py` | Файл поставки | 2d8a1086c0d5d31d2a61b50a99839bcd775fce0ea96fc49de021569d26c63562 |
| `modules/self_development/EXPERIENCE.md` | Файл поставки | 2d7d1520e1d75a76c55ca3271c8220f10482316a29d82d46354be9a271ee0ce0 |
| `modules/self_development/GUIDANCE.md` | Файл поставки | 38998e5c243c4a92c9d014ea193cc1b36fdbb6b9ad2a5486161fb902ea9b7586 |
| `modules/sources/CONTRACT.md` | Файл поставки | 95c7617b371a11756f84e3dc436be7c5e424e94781d395b97065173e2596704f |
| `modules/sources/GUIDANCE.md` | Файл поставки | a1d32f98892fdfdd8b53a3000a2ddbe9e20a85a426e878c2f8074c97b4c507d8 |
| `modules/sources/REGISTRATION.md` | Файл поставки | 3a3cea44fc767ee06eaad12c9f00fdcd9c629c88af72126a05cb9212d6beaebd |
| `modules/sources/api.py` | Файл поставки | 9baede73e20499df1ad3883e2da2e969f86dbe73232a58e450083e1ffd0a3850 |
| `modules/sources/repertoire.py` | Файл поставки | f229e8801612d4d402076dfc96d959c753355402859e553362c8292b54bb0ed3 |
| `project/README.md` | Файл поставки | 3945b1bda18f4b0a764db5fa6677b698b832524955a7a3c384dd0767cdc7d8be |
| `project/artifacts/.gitkeep` | Файл поставки | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `project/handoff/.gitkeep` | Файл поставки | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `project/source/.gitkeep` | Файл поставки | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `source/external-dpf/.gitkeep` | Файл поставки | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `templates/BOUNDED_EXECUTION_PROFILE_TEMPLATE.md` | Файл поставки | a52d6043394c38aed93b42b7f629bf1c8fde36dd21abfaba837cb2b61c22d9e1 |
| `templates/DPF_CONTRIBUTION_RESOLUTION_TEMPLATE.yaml` | Файл поставки | fa57c7307b90e39c8e62887b8d5ccdf180983cf2ed69a752221650f6c1db3821 |
| `templates/DPF_REPERTOIRE_TEMPLATE.yaml` | Файл поставки | 79cd2d60af505cb0100346a553e2edfba738c2945c2bdfe6c1111cc9831a3ace |
| `templates/POST_INITIATIVE_LESSONS_REVIEW_TEMPLATE.md` | Файл поставки | 2132c0d8657d051467831648c571af6b4858c6e630c3f21fc9d79ef825a190da |
| `templates/RUNTIME_CAPABILITY_PROFILE_TEMPLATE.yaml` | Файл поставки | bf60c842e513c050d0ff436a9ff30129b5b76f049a0d4fdd6e17a1e5b66680d2 |
| `templates/STATE_INDEX_TEMPLATE.yaml` | Файл поставки | b8917fcd018b830585a338337e82f865060bbb11ab4211ca55ea4afa90ff41e7 |
| `tools/package/integrity.py` | Файл поставки | a53733ce2015d2071b08116c90b09f99f070cac81924edb6ebfec26271d0cec3 |
| `tools/package/prepare.py` | Файл поставки | b54199c155b3866059a37534236f14fadceb582592c0071e3aeff0a8d9736d17 |
| `tools/package/verify_configuration.py` | Файл поставки | 96e8df954f0f7fdb2afbc60099d47c63e08ff902766d2adca1d5ca50f122e812 |
