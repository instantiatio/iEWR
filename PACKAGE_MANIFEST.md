# Состав iEWR 5.7.0 Beta

Точная поставка: 142 файла. Исходная опубликованная основа — iEWR 5.6.4 Beta. Добавлен только пустой project/dpf/.gitkeep для первой регистрации. Ведомость различает роли и фиксирует bytes; пригодность и пределы проверок — в VERIFICATION.md.

| Файл | Назначение | SHA-256 |
|---|---|---|
| `AGENTS.md` | Действующая инструкция, статус или evidence этой редакции; не universal grant | 25ad811c9d95b64bd74a1161570fed89ce3a44f539eac4100c9e5d50c64ba29b |
| `BASELINE_STATUS.md` | Действующая инструкция, статус или evidence этой редакции; не universal grant | 4ac4c9ba4251059c56f08e1f88ecb414b8729f63685d86767c09e7a731f2c5a1 |
| `LICENSE` | Лицензия и атрибуция; сохранены bytes | ef4da070e506cd1018f449fc78bae57537b96f797264cf56f133e411b5b611ec |
| `MODEL_SELECTION_RECOMMENDATIONS.md` | Инструкция применения либо указатель; scope задан содержанием | b7059b78fd8a6d90e677520fbaf880ce6ef0634855e597d56847f590fec43490 |
| `README.md` | Инструкция применения либо указатель; scope задан содержанием | e72bef5c490afb20ba43d4ab8b4bab19371f6124436b3f33a6f9871f3716403c |
| `RELEASE_HISTORY.md` | История и bounded migration; не текущие grants | bd65002749bf994e14a9291401125ac09cbe49c67348244d02d29e4f05310934 |
| `RELEASE_NOTES.md` | Действующая инструкция, статус или evidence этой редакции; не universal grant | b72b4708dda7a3280ca56dd15fd102c8ea9a277aec6feff1bb8382014aed8bef |
| `VERIFICATION.md` | Действующая инструкция, статус или evidence этой редакции; не universal grant | 924449e018f407c5cfb10a22b08eebdd85fdae279f4dccbf75f8bf84148dc0db |
| `adapters/ADAPTERS.md` | Инструкция применения либо указатель; scope задан содержанием | f65439a96ef3a053e1c21ea9efc694b947f2171d4b6efd016f28be641656af00 |
| `adapters/agent_host/channel.py` | Программный consumer/helper; роль и границы по owning guidance | 115d747d2dbb037cf2e6f1a912ccb939d5c347343eb47d92db8e751a478f0390 |
| `adapters/agent_host/responses.py` | Программный consumer/helper; роль и границы по owning guidance | 6dc5ca67a3f081248c6717e512dc87b87d3f7f2dd6cb0a997354fad2889323dd |
| `adapters/filesystem/artifacts.py` | Программный consumer/helper; роль и границы по owning guidance | f5309420636b03486c62232d5ed1e7d19239a39fc567bfb2776cb1fe9261ae20 |
| `adapters/filesystem/local.py` | Программный consumer/helper; роль и границы по owning guidance | 5f0bd1dde5f6e3d8ea44609b6c6d53c9e57ae93838e3ba7b664e79893f22a0c0 |
| `adapters/filesystem/recovery.py` | Программный consumer/helper; роль и границы по owning guidance | b2114cef513b4ac734f39d3668b2cff857126129fc0b0fd340cafee7dd52ccd2 |
| `adapters/filesystem/repertoire.py` | Программный consumer/helper; роль и границы по owning guidance | 6455cfc4862c05b354c70a3723628ecb13e4b37141d6ef5363d3b459327e253a |
| `adapters/filesystem/repertoire_engine.py` | Программный consumer/helper; роль и границы по owning guidance | 85b6a113bdbb1b15ffa5775a5542b226d6a37b2874f4a51987032957073a6463 |
| `adapters/presentation/text.py` | Программный consumer/helper; роль и границы по owning guidance | 84442e0aa5a586610717f5f66dce9e91cc37d7e8969f2f8bfa9876b386d41415 |
| `app/bootstrap/CONFIGURATION.json` | Действующая инструкция, статус или evidence этой редакции; не universal grant | 24ac5d5d3792511dab59ed07fbac5fb6b34ac425ea8eea5dad17015c0fe5cfee |
| `app/bootstrap/ENTRY.md` | Инструкция применения либо указатель; scope задан содержанием | 77b24e3dcddf998be34331a14d130e680f7a3ebda969f86e697bb5bc29f25f2c |
| `app/bootstrap/operation.py` | Программный consumer/helper; роль и границы по owning guidance | f4da43f3458c417bab08c968f06e7a7f3dbaeab3c1ce707095736d90aa30c780 |
| `app/bootstrap/recovery.py` | Программный consumer/helper; роль и границы по owning guidance | 432cb6a56abee240d6c3d25fa4565537dabc6bf790e10a9a4bdbd45472ca108d |
| `catalog/README.md` | Инструкция применения либо указатель; scope задан содержанием | 4dc9b22f7edbba969411737f0574cefedd9f863caa47c36a507e57b27b59c4ea |
| `catalog/dpf/METHODS.md` | Инструкция применения либо указатель; scope задан содержанием | a86566bbfda7c846a1011146d5689e0f7a8a51c9e0f6c1ae47ec91c9e92a6997 |
| `catalog/engineering_views/CATALOG.md` | Инструкция применения либо указатель; scope задан содержанием | 04362cc56908a077c47d206a9064501c8285341e6285f38352a0760db5a5ae34 |
| `catalog/engineering_views/README.md` | Инструкция применения либо указатель; scope задан содержанием | 0576c71190c4eac933529532d9a1ca9e91a435593ca50b1117f0e6f881099c00 |
| `catalog/engineering_views/templates/PROJECT_VIEW_PROFILE.yaml` | Условный carrier; только при названном use | 96a70940fa3a6d1aa0130481337ada9b05573923f2797f7e9ff6dc2ae2b970b6 |
| `catalog/working_process_compositions/CATALOG.md` | Инструкция применения либо указатель; scope задан содержанием | 35618f6dc9c84bf782321daa6ab8e12794f4f3cb4a9c2d9102cd75757596c472 |
| `catalog/working_process_compositions/README.md` | Инструкция применения либо указатель; scope задан содержанием | 6e2585504014ba917c4acf7b39bd5c104fcb203a841f50b2e4805d5db2b4ce76 |
| `catalog/working_process_compositions/templates/WORKING_PROCESS_COMPOSITION_RECORD.yaml` | Условный carrier; только при названном use | 4ae37efc59297fc6d2700799ef484143f825c7c8e4c6a7b2f6879c9da3bdd449 |
| `docs/BUNDLED_DPF_BASELINE_REFRESH_AND_INTEGRATION_GUIDE.md` | Инструкция применения либо указатель; scope задан содержанием | 5bc4cd7bbb1626dd5d7e5c1e8d5ca1b98b16b54057d4914d0908990c90e5925f |
| `docs/DPF_FORMATION_METHOD.md` | Инструкция применения либо указатель; scope задан содержанием | 6dde101b5f524a5686237aacf519d8e5c431cf3d79bd56ed90a86fd1e8032e04 |
| `docs/DPF_REGISTRATION_GUIDE.md` | Инструкция применения либо указатель; scope задан содержанием | 1213430c97cc37ac9f892b9cf400c910917be43e7efb9f7b5c83ed8649e451eb |
| `docs/EWR_CORE_ARCHITECTURE_CONTRACT.md` | Неизменённый governing Core Contract 1.0 RC | ea9842606c82af26b3217fae8d743e99e0030ec56ce089b69ad25c551b65343c |
| `docs/FPF_CONNECTION_GUIDE.md` | Инструкция применения либо указатель; scope задан содержанием | e67d3d853a25b1dcfccea3912d1695ca60c5418dfd8d202d7fdb2cbf10736319 |
| `docs/HUMAN_AI_SOURCE_CONTRIBUTIONS.md` | Инструкция применения либо указатель; scope задан содержанием | 08be50486a1efa3790e78f33fad8443d8ea314aef827e7db24bef85e8ec57118 |
| `docs/MIGRATION_5_3.md` | История и bounded migration; не текущие grants | 83434fbf734e50959cd902187e4bb00144de80f042e0769ec7e20a476ccd8217 |
| `external-sources/external-dpf/.gitkeep` | Пустой слот предусмотренного проектного/source locus | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `external-sources/fpf/.gitkeep` | Пустой слот предусмотренного проектного/source locus | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `frameworks/dpf/LICENSE` | Закреплённый внешний источник, его binding или атрибуция | 9e5f1b3c610b9c2da5c313bf81d577a7d1acec686bdb0384edefa6df0f90cd94 |
| `frameworks/dpf/LICENSING.md` | Закреплённый внешний источник, его binding или атрибуция | f80502802237f19a0ea85303a792281e0f9c533e86d23f8a6174d5c18bd70864 |
| `frameworks/dpf/NOTICE.md` | Закреплённый внешний источник, его binding или атрибуция | f5d90542532eac93eaf87ad62c5568b1e92a8c98638b975f3b1b82d88c3553cb |
| `frameworks/dpf/REPERTOIRE.yaml` | Закреплённый внешний источник, его binding или атрибуция | 1d04abe4326eea8e49c68ef538465c830e6c61b263d3a45bc6ff3ec6cd837f0c |
| `frameworks/dpf/checklist/2026-09-25-rev-9e1c4834/CHECKLIST-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | 503da6fef65ee02de0e8ce41c2600479a2ce7e6163f3cb5ea6f09d6c026ce679 |
| `frameworks/dpf/development-opportunity-construction/2026-09-20-rev-9e1c4834/DEVELOPMENT-OPPORTUNITY-CONSTRUCTION-AND-DEVELOPMENT-DIRECTION-ADVISING-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | a0fe9a5fe0564c0b223cff8ac3bcf99828cbeef7e4e9c57919a05a34fd2afb61 |
| `frameworks/dpf/explanation-design/2026-09-20-rev-9e1c4834/EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | db4111b53650e22c73eee9e4999e7860873f61a2c362a76e1493ca7d290fd929 |
| `frameworks/dpf/instantiatio-sdlc/0.2.2/Instantiatio SDLC DPF.md` | Закреплённый внешний источник, его binding или атрибуция | 7669b7b8903c36ab9bdef5f723c60077bd92b84cd9471be53e5b97e0860e548a |
| `frameworks/dpf/instantiatio-sdlc/0.2.2/README.md` | Закреплённый внешний источник, его binding или атрибуция | 68ff32665e5bafa9f7db91e2177520810b2123bbd76948176e3fee215cf9ce17 |
| `frameworks/dpf/instantiatio-sdlc/0.2.2/SOURCES.md` | Закреплённый внешний источник, его binding или атрибуция | a98a90b5cd9ab066d83a468cb8fe67680ad2a38a5514954c37feb3faadd462aa |
| `frameworks/dpf/instantiatio-sdlc/0.2.2/SOURCE_LOCATORS.md` | Закреплённый внешний источник, его binding или атрибуция | 4d47f92f8f05f6b0fa8612a8b73e6e92ef0763266df8c56f64b8850a147fa01a |
| `frameworks/dpf/knowledge-corpus-access-engineering/snapshot-2026-10-04-rev-9e1c4834/KNOWLEDGE-CORPUS-ACCESS-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | 9d47ff7f0ffa2c00df03cf4a4fdf2fc2d8ef7f0a6e8701fed1eb6fb481fb05cc |
| `frameworks/dpf/method-engineering/2026-09-20-rev-9e1c4834/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | 15e74fa6fcc5aeed7492cda684f04a619e333c99df3a50931c1f873d832851f6 |
| `frameworks/dpf/operations-management/2026-10-02-rev-9e1c4834/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | c89531b2727190602fe4c61dbebf817e1ffb47a81135b36427ca00d635cbd390 |
| `frameworks/dpf/organization-administration/2026-09-20-rev-9e1c4834/ORGANIZATION-ADMINISTRATION-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | 917ddcfad30b96319956c8bdae58a5df18e6c64d34cf62953ac7f2df9678fa96 |
| `frameworks/dpf/organization-change-engineering/2026-10-03-rev-9e1c4834/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | fc4994ff19de7fa86743f10af355de45bb4622090258b3c5d8e123e24d8708ce |
| `frameworks/dpf/problem-structuring-decision-support/2026-09-26-rev-9e1c4834/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | ab7a8369b38086bc08acd0aad5157325ef07eeda2f8b9b4a10f9e85f3e08b4fa |
| `frameworks/dpf/research-method-practice/2026-10-04-rev-9e1c4834/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | 5c4e9a9077cf5ffabcb87517901982c39b9c1419937ef24c027bb37b23e30df3 |
| `frameworks/dpf/semantic-integration-engineering/2026-09-20-rev-9e1c4834/SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | a16e8b39298dbd8b00175684260ba012ef18c9d4de59fc8717e8f7c313ba7889 |
| `frameworks/dpf/strategy/2026-09-20-rev-9e1c4834/STRATEGY-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | 761bf91eedeb0ee79f247d620411989586661387790e7d52a4d34958bfc18977 |
| `frameworks/dpf/systems-engineering/2026-10-03-rev-9e1c4834/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | Закреплённый внешний источник, его binding или атрибуция | b0d0698eabc54da9b444195aac110484c7b08de923b8d0e9117efd8367140f38 |
| `modules/coordination/CONTRACT.md` | Ограниченное историческое B1 описание; не общий lifecycle | 66a8cad0e6839587d48025c8e0840ff83c37e1d6a7638f40bd0e034e9bcaeebd |
| `modules/coordination/GUIDANCE.md` | Инструкция применения либо указатель; scope задан содержанием | 5fc0479d7787ca8d09242c529c78f0c62f16b15cfb87c7d13c8a34895c4fae54 |
| `modules/coordination/api.py` | Программный consumer/helper; роль и границы по owning guidance | eb5de62e634e210b777a2a9ccea80cf528c9c50a5c127f39816f3a90e02ebe88 |
| `modules/effects/CONTRACT.md` | Ограниченное историческое B1 описание; не общий lifecycle | 38339720cde001c4af4af3eac242af2e8395f13dd2d7a156efc14644c4c8f44b |
| `modules/effects/GUIDANCE.md` | Инструкция применения либо указатель; scope задан содержанием | 6aef670f0a9c303e69a97f0afa03a4d83e3ed66bf4cea5ddf51a8eef31e55cde |
| `modules/effects/api.py` | Программный consumer/helper; роль и границы по owning guidance | 054142aaea6287187238cf97dcd1f9d3a852224d77360b6daa907a375155a3bf |
| `modules/effects/operations.py` | Программный consumer/helper; роль и границы по owning guidance | ec2be5ef2b71b9836772ffc935a95724104e8b7f63ce2f5511035efd6ee699f6 |
| `modules/execution/CONTRACT.md` | Ограниченное историческое B1 описание; не общий lifecycle | 1aabccabf4a4674080dce494918920466ebb4d14fe3fde14d3758405a0f09cee |
| `modules/execution/EXECUTION_BASIS.md` | Инструкция применения либо указатель; scope задан содержанием | 91a7e1d7df78bb705b289c61169ce71f68f94e2b7c5515c570a291d9e882b3f5 |
| `modules/execution/api.py` | Программный consumer/helper; роль и границы по owning guidance | 5f50847385764a116a0042465926b9ba5cfe45938d8de68a3bb680ec89ccc9b0 |
| `modules/execution/operations.py` | Программный consumer/helper; роль и границы по owning guidance | af38d55cf76b4472977fa6d7369bfac6358e019cd6a0fc8155254123db7bd66e |
| `modules/execution/profiles.py` | Программный consumer/helper; роль и границы по owning guidance | 3ee357c210793301b48bf12ca7ba64b6683cb6ced75ca54620cfc02e4b7c8fca |
| `modules/execution/work_basis.py` | Программный consumer/helper; роль и границы по owning guidance | d96f29cf52f4474b99b572daa29be14e2367f0b5045c7fe0cb68dd0a4428e16b |
| `modules/formation/CONTRACT.md` | Ограниченное историческое B1 описание; не общий lifecycle | 604d41cb8c9b80d299830f276411a02cc1f00ee441a67eaa5159451b41870ba8 |
| `modules/formation/DOMAIN_WORK.md` | Инструкция применения либо указатель; scope задан содержанием | 24cefcf3173f200b4151bbae24020e2b8b9e540bdcb2f48d973e2572f7b21682 |
| `modules/formation/api.py` | Программный consumer/helper; роль и границы по owning guidance | c2ffb6dd62fa3fec34b6e06fb5ce369091653ea26778965b6ad342788f8f2bc1 |
| `modules/formation/execution_basis.py` | Программный consumer/helper; роль и границы по owning guidance | 01b3ac1d646126ed42f13a7b21878f597603b7986a0959f89279056d8ad60440 |
| `modules/formation/operations.py` | Программный consumer/helper; роль и границы по owning guidance | 2d32a3f45424d43e3fd29e8a217c10b882150ad23d11860a3ec42d8d27279573 |
| `modules/governance/CONTRACT.md` | Ограниченное историческое B1 описание; не общий lifecycle | 93a666400239dcf6b9ccbcb8855032fc93e3ae5899ebc232a331461c87acf5b3 |
| `modules/governance/GUIDANCE.md` | Инструкция применения либо указатель; scope задан содержанием | 76c18e071cb671d121b438dcfdc771c60d0c2e14fd458a862a5bf963d9951fc5 |
| `modules/governance/api.py` | Программный consumer/helper; роль и границы по owning guidance | aa7fa47660da19204449452102ec8586a87ea1ab08b9e17514f8ea47815ca6ca |
| `modules/governance/operations.py` | Программный consumer/helper; роль и границы по owning guidance | 8a28acc269b1c6ea82b86b990fd9560e7b2574a728643435b15d3c32e302927e |
| `modules/governance/responses.py` | Программный consumer/helper; роль и границы по owning guidance | 1a504b5f5bf2dcad82df295270df48b91a33dab715c70f94e168a370a47cf891 |
| `modules/interaction/CONTRACT.md` | Ограниченное историческое B1 описание; не общий lifecycle | d149e12fd6a373551d09a9620933b8b5a40ecd555c89e4024cc72406dca19439 |
| `modules/interaction/DECISION_VIEW.md` | Инструкция применения либо указатель; scope задан содержанием | d1f6d0717f6416380d2730bc2b62017e7a3d24fda6f2a4a7ab00aef8b7561719 |
| `modules/interaction/HUMAN_INTERACTION.md` | Инструкция применения либо указатель; scope задан содержанием | 1f30aa9b325a9b895db24e73360fd2d117b9c6aa2cf13b22955cf6e91785f3a5 |
| `modules/interaction/HUMAN_VIEWS.md` | Инструкция применения либо указатель; scope задан содержанием | 92aa0d7a6c0512b9dbb22977dc2a591d21cce4620f9afc68a74145b7f13416b2 |
| `modules/interaction/api.py` | Программный consumer/helper; роль и границы по owning guidance | 57c2ef8e1926c0f37a0c158b5eebef315c060b6aad94726eb7f3209fbd56a5a0 |
| `modules/interaction/preferences.py` | Программный consumer/helper; роль и границы по owning guidance | de98c54aa3652bb5518442a6f8c174dfce7c8c3c0ccbd66c0b7f80eeb7356d99 |
| `modules/interaction/presentation.py` | Программный consumer/helper; роль и границы по owning guidance | c4749c9cac50683383d29cbf85bd03339a32ea164ea5b901273d97398edadd49 |
| `modules/recovery/CONTRACT.md` | Инструкция применения либо указатель; scope задан содержанием | bd24400c9c305d237eb52de519c3ae20c86ae9d1eb0ae383e3b2efd517cb4a58 |
| `modules/recovery/api.py` | Программный consumer/helper; роль и границы по owning guidance | 904e137c2daf4134848307b2025daf7f2407ef71c3cceacdb4e5b817078a9215 |
| `modules/reliance/CONTRACT.md` | Ограниченное историческое B1 описание; не общий lifecycle | 7458f8dd2d291a510ec20520dc454d890d80da0aae62b379bdaa5e74f2c42674 |
| `modules/reliance/RECEIVING_USE.md` | Инструкция применения либо указатель; scope задан содержанием | aad4ebc2300033ecaf4ad2f2b4024151b75802719875fb8c25edf64eaade6634 |
| `modules/reliance/api.py` | Программный consumer/helper; роль и границы по owning guidance | fc0b842468dc11dd5f5bb2ee902697e62294699de097354010602d95370d28a9 |
| `modules/reliance/assessment.py` | Программный consumer/helper; роль и границы по owning guidance | 2d8a1086c0d5d31d2a61b50a99839bcd775fce0ea96fc49de021569d26c63562 |
| `modules/self_development/EXPERIENCE.md` | Ограниченный maintainer reuse прежних наблюдений | c3ab0800fd043affc836fc2bf7ab5f2a6de8744a521076e9a5ed8740debe4e3f |
| `modules/self_development/GUIDANCE.md` | Инструкция применения либо указатель; scope задан содержанием | b14287f05a88d4af7aabb798dfaecd3400c6741de73edaf4b6013431247f93d1 |
| `modules/sources/CONTRACT.md` | Ограниченное историческое B1 описание; не общий lifecycle | 95c7617b371a11756f84e3dc436be7c5e424e94781d395b97065173e2596704f |
| `modules/sources/GUIDANCE.md` | Инструкция применения либо указатель; scope задан содержанием | 6ae71ffb7d619892bffd6f3f10235822f4657d510e4d443be3b8f8e71be4ed09 |
| `modules/sources/REGISTRATION.md` | Инструкция применения либо указатель; scope задан содержанием | d443f1bae4aad76cdeb4ac0c1727771d5483747a1bf6557fe6382e177bac30d7 |
| `modules/sources/api.py` | Программный consumer/helper; роль и границы по owning guidance | 9baede73e20499df1ad3883e2da2e969f86dbe73232a58e450083e1ffd0a3850 |
| `modules/sources/repertoire.py` | Программный consumer/helper; роль и границы по owning guidance | f229e8801612d4d402076dfc96d959c753355402859e553362c8292b54bb0ed3 |
| `project/README.md` | Инструкция применения либо указатель; scope задан содержанием | b25656acdc2d849f16a446c74b34b407fdf9ab5dbee3d1b7d13eaa324a4201cd |
| `project/artifacts/.gitkeep` | Пустой слот предусмотренного проектного/source locus | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `project/dpf/.gitkeep` | Пустой parent первой project repertoire registration; не index или initiative | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `project/handoff/.gitkeep` | Пустой слот предусмотренного проектного/source locus | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `project/source/.gitkeep` | Пустой слот предусмотренного проектного/source locus | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `templates/BOUNDED_EXECUTION_PROFILE_TEMPLATE.md` | Условный carrier; только при названном use | 6e7d9232c635af214ac87467d9bdc52fcaae95738dc85568c87649fc7260a58b |
| `templates/DPF_CONTRIBUTION_RESOLUTION_TEMPLATE.yaml` | Условный carrier; только при названном use | fa57c7307b90e39c8e62887b8d5ccdf180983cf2ed69a752221650f6c1db3821 |
| `templates/DPF_REPERTOIRE_TEMPLATE.yaml` | Условный carrier; только при названном use | 79cd2d60af505cb0100346a553e2edfba738c2945c2bdfe6c1111cc9831a3ace |
| `templates/POST_INITIATIVE_LESSONS_REVIEW_TEMPLATE.md` | Условный carrier; только при названном use | 2132c0d8657d051467831648c571af6b4858c6e630c3f21fc9d79ef825a190da |
| `templates/REENTRY_BINDING_TEMPLATE.json` | Условный carrier; только при названном use | 096d5e213606ff53689ea51ef9bf62b8d6210e6f1acab41e65e5a5009d2a2c8e |
| `templates/RUNTIME_CAPABILITY_PROFILE_TEMPLATE.yaml` | Условный carrier; только при названном use | 7f533d3fd70528fdfe227449a497013b901e14e1b085b45c0bc1d26111a16060 |
| `templates/STATE_INDEX_TEMPLATE.yaml` | Условный carrier; только при названном use | b8917fcd018b830585a338337e82f865060bbb11ab4211ca55ea4afa90ff41e7 |
| `tools/decision_view/README.md` | Инструкция применения либо указатель; scope задан содержанием | 36b0b8fbfedc5a58ffb89af6a03fb226e3c43c3716c56006052459944342cc66 |
| `tools/decision_view/THIRD_PARTY.md` | Лицензия и атрибуция; сохранены bytes | 5b84fac0031b6eeafcd8aa46e5d5ce6378feab05a2cd5a809c0e3f0f15a41176 |
| `tools/decision_view/app.js` | Неизменённый ресурс представления/helper | 55b416368f721648c7e06cef06215d3d9a2a6b57e5b1aed2cce9babecbe4f778 |
| `tools/decision_view/build.py` | Программный consumer/helper; роль и границы по owning guidance | 3c7500351360f3bbba2bc3f9061c387598b96bdbec423f4b988710693ae07b41 |
| `tools/decision_view/er.py` | Программный consumer/helper; роль и границы по owning guidance | 32085bf41185b7dce5555088cf928d5d850b07bf3af022822dd40920de940d1a |
| `tools/decision_view/examples/orders.er.json` | Binding, данные, пример или template; не authority | 5563ebd4b1cd49ebd678c3df1a06ef8f7d8b9652d3a089577a9ac458ea6a1ffc |
| `tools/decision_view/examples/question.json` | Binding, данные, пример или template; не authority | 2fad708b235636da42a369bd08775a2634dba391d805ae6340a4024359c4dae9 |
| `tools/decision_view/page.html.in` | Инструкция применения либо указатель; scope задан содержанием | 820309c3e9f09225fc3b480608628884e2c13481972c6fa3bc85005ce930f7c1 |
| `tools/decision_view/pending.py` | Программный consumer/helper; роль и границы по owning guidance | 4a0c1b06bbf1bd29179d0d527a64f201050428ec31e698857daf5f2e8a0b41c3 |
| `tools/decision_view/receive.py` | Программный consumer/helper; роль и границы по owning guidance | 5a1c4e817843cfb3fe235ff535985e2439d3964a906440b847893e16e3c601d2 |
| `tools/decision_view/render_markdown.cjs` | Инструкция применения либо указатель; scope задан содержанием | ea1b237dd8638ed28a06fa77722602dfc53a36d0cf9c566b9273f2fe9a8bc5e6 |
| `tools/decision_view/snapshot.py` | Программный consumer/helper; роль и границы по owning guidance | bdd1983d1f20b190347caed536402f2fc1c5e24b3c1c07f093d2c6cc76885e07 |
| `tools/decision_view/style.css` | Неизменённый ресурс представления/helper | 8365e6443586b4fc9642b9f3e43f3739575f7473c9c099506ffadee0bd7afae6 |
| `tools/decision_view/vendor/MARKED_LICENSE.md` | Лицензия и атрибуция; сохранены bytes | 8e3a3f82f59a60958f56ca08f445647c32a4733dc7ca6c2c46f6eb898471ab9c |
| `tools/decision_view/vendor/marked.cjs` | Инструкция применения либо указатель; scope задан содержанием | 0db7abc826b5ac76f6ed11951ae34074ba50438ce6ea8d52889203779e5cbbad |
| `tools/fpf/access.py` | Программный consumer/helper; роль и границы по owning guidance | 4537e0a17a9341a76ed497c9bc56145247486244829ba7bbbe124c066793c030 |
| `tools/human_view/README.md` | Инструкция применения либо указатель; scope задан содержанием | fe332a0383df8f9aa4e5ce7a776af5fdda114b9f0fe7e2ed446df73e22fe3c66 |
| `tools/human_view/build.py` | Программный consumer/helper; роль и границы по owning guidance | 7f94e7416c9b29ba1832517cab9dc8a4e3bdf0e0f2d98eda2d81dc93069ccfcc |
| `tools/human_view/examples/change.json` | Binding, данные, пример или template; не authority | 6bc98a01ffefd379281663532f93c04e699bdfa23b6ea758ff3da35ea9caa70a |
| `tools/human_view/examples/observations.json` | Binding, данные, пример или template; не authority | 3e877908cce6f102859415f69b47efb6e88b5c6c6cdc9d97272c8a145a92f6db |
| `tools/human_view/examples/plan.json` | Binding, данные, пример или template; не authority | 568647ef1a2e0602f7ba3537a5b04b2ed427188a445805ea640f255461aebf51 |
| `tools/human_view/examples/result.json` | Binding, данные, пример или template; не authority | bd6012fa4cd705b8d46f03b7976a64e3aaa48b0685b9f9a76bcb67aa51032501 |
| `tools/human_view/examples/review.json` | Binding, данные, пример или template; не authority | f9e00064fb0dd28b713749b3bdd406fec9e4c3c7ac43ab475f1f3c8ab9d7a42b |
| `tools/human_view/examples/situation.json` | Binding, данные, пример или template; не authority | a1398fb7e2a512bbbdbf34445baf7ed44e543a812ab5302650da889a9cf05f9f |
| `tools/package/integrity.py` | Программный consumer/helper; роль и границы по owning guidance | 84b4e0d19aba146e93768662c5c7a94958ee40e883b915ddd3488ad6adda41ec |
| `tools/package/prepare.py` | Программный consumer/helper; роль и границы по owning guidance | 3dab910958c0a5492a005bac1669e15b1e314306b93c67440112b8f4e2f7c695 |
| `tools/package/verify_configuration.py` | Программный consumer/helper; роль и границы по owning guidance | 96e8df954f0f7fdb2afbc60099d47c63e08ff902766d2adca1d5ca50f122e812 |
