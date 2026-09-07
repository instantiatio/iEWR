# iEWR 5.2.1-beta — exact candidate package

| Field | Value |
|---|---|
| Package ID | `iEWR-5.2.1-beta` |
| Version | `5.2.1-beta` |
| Status | Closed Beta candidate for Human acceptance; not yet accepted |
| Source baseline | accepted local `iEWR-5.2.0-beta`, 96 files; not published |
| Source ZIP SHA-256 | `3d6eb16840e1d36b48825bced4f880eb23bda713d7de60925cb4c1c045db0f1d` |
| Architecture | Core Contract 1.0 RC, owner APIs and runtime semantics preserved; bounded interaction instruction clarification |
| Bundled DPF | author date 2026-09-05; explicit licensing revision `2026-09-05-rev-d514a6fc` |
| distribution_ready | `false` |
| Public release | not performed; separate Human request required |

Exact changes, evidence scope and remaining limits: [BASELINE_STATUS.md](BASELINE_STATUS.md).
Licenses/attribution: [upstream NOTICE](frameworks/dpf/NOTICE.md), separate [iEWR LICENSE](LICENSE).
Interaction guidance applies to ordinary work. Self-development support still
requires explicit development of iEWR. Neither creates a runtime owner, workflow,
authority or automatic source/reliance transition.
Local SDLC remains unchanged and experimental; no SDLC overlap audit.

Only this exact inventory is the product. User source/reference files, development
records/tests, candidate ZIPs and handoff archives are excluded. Empty scaffold
and project/README are the only project members. Manifest has no self-hash;
its SHA-256 and ZIP identity are recorded in external delivery evidence.

## Exact file inventory

96 selected files; 95 hashed rows; 94 configuration rows.

| Path | Role | SHA-256 |
|---|---|---|
| `AGENTS.md` | selected product component | fb208c4dc80a0c0958f60e95c88f7777101497328583e72e0e5f3c53ba2fdc7a |
| `BASELINE_STATUS.md` | selected product component | 36db6fc5647a9e91d2d898d67d4a89c5578b3d14b21b4dbf249f451e3c078354 |
| `ENGINEERING_WORK_BOOTSTRAP_GUIDE.md` | selected product component | 3105d704e1af6f5fa824d24b6b9347b18fec7e21a1fe71f1666ca1fad5e27999 |
| `LICENSE` | selected product component | ef4da070e506cd1018f449fc78bae57537b96f797264cf56f133e411b5b611ec |
| `MODEL_SELECTION_RECOMMENDATIONS.md` | selected product component | b7059b78fd8a6d90e677520fbaf880ce6ef0634855e597d56847f590fec43490 |
| `README.md` | selected product component | 86cf726cb9c7872fb0bf189cb0fccb8b181c11ad080a80980dec0d3554fc5225 |
| `WORKING_PROCESS_AND_LOOPS_GUIDE.md` | selected product component | 60f642ae1eb19a05669a7f0c86e6ba65a0e47f186718df41c85cf6fce097f557 |
| `adapters/ADAPTERS.md` | selected product component | 97a1c96747e2911878a03928e24c508bbb956e6fe0edb450a43a35df12fe396d |
| `adapters/agent_host/channel.py` | selected product component | 115d747d2dbb037cf2e6f1a912ccb939d5c347343eb47d92db8e751a478f0390 |
| `adapters/agent_host/responses.py` | selected product component | 6dc5ca67a3f081248c6717e512dc87b87d3f7f2dd6cb0a997354fad2889323dd |
| `adapters/filesystem/artifacts.py` | selected product component | 635a03a3784356241ff20087dbe8e9343cf75eb8edcd285c609e9f4fc3240a23 |
| `adapters/filesystem/local.py` | selected product component | c571a45b534b51a68c45a9ceadfbd2f3613491879197eaa30e62894513af34d2 |
| `adapters/filesystem/recovery.py` | selected product component | 9112729bb1f4b7abd219f9f4d0a77300ac6ae3986c8593b8e379625d92a31ba6 |
| `adapters/filesystem/repertoire.py` | selected product component | 025559c5cfcccf766c37bd4b198dbff21d7ce6d558780fa6c6636f43a50b5d43 |
| `adapters/filesystem/repertoire_engine.py` | selected product component | 21bdde5b57e80544b49ea588ca246099955afcd71b9525bc3135a0652ece53fd |
| `adapters/presentation/text.py` | selected product component | 84442e0aa5a586610717f5f66dce9e91cc37d7e8969f2f8bfa9876b386d41415 |
| `app/bootstrap/CONFIGURATION.json` | selected product component | 84370492d4a7e768e0dd02159cf63736956066332242a9bc2ec78bc8dcd6fe39 |
| `app/bootstrap/ENTRY.md` | selected product component | 5f9851ed231c3235176c4e9efc03d254d19b8d71e0284c7502b18137d2a1e224 |
| `app/bootstrap/operation.py` | selected product component | 6fde3ea71cfcb8c9039c711713e60116bf56c9316370b50d91a61a9c056a0d5f |
| `catalog/README.md` | selected product component | 59e93386563b70b8a271d01ead116f99e9455e0ce17bd59dda4d5082e6e5b9e9 |
| `catalog/engineering_views/CATALOG.md` | selected product component | 04362cc56908a077c47d206a9064501c8285341e6285f38352a0760db5a5ae34 |
| `catalog/engineering_views/README.md` | selected product component | 0576c71190c4eac933529532d9a1ca9e91a435593ca50b1117f0e6f881099c00 |
| `catalog/engineering_views/templates/PROJECT_VIEW_PROFILE.yaml` | selected product component | 96a70940fa3a6d1aa0130481337ada9b05573923f2797f7e9ff6dc2ae2b970b6 |
| `catalog/working_process_compositions/CATALOG.md` | selected product component | 35618f6dc9c84bf782321daa6ab8e12794f4f3cb4a9c2d9102cd75757596c472 |
| `catalog/working_process_compositions/README.md` | selected product component | 6e2585504014ba917c4acf7b39bd5c104fcb203a841f50b2e4805d5db2b4ce76 |
| `catalog/working_process_compositions/templates/WORKING_PROCESS_COMPOSITION_RECORD.yaml` | selected product component | 4ae37efc59297fc6d2700799ef484143f825c7c8e4c6a7b2f6879c9da3bdd449 |
| `docs/BUNDLED_DPF_BASELINE_REFRESH_AND_INTEGRATION_GUIDE.md` | selected product component | 610573e28fb9bfa55b26196622a27bf00aab4d5a885b0fa06b900fee17314114 |
| `docs/DPF_FORMATION_METHOD.md` | selected product component | f5720bc446534877da42fa63b5c7c30de7e38110e8c7bbd17839735450bd8b52 |
| `docs/DPF_REGISTRATION_GUIDE.md` | selected product component | 0c6ae68196ed93d337bd492a93bc5b94832e41c780c45c28ce643151d91c6d48 |
| `docs/EWR_CORE_ARCHITECTURE_CONTRACT.md` | selected product component | ea9842606c82af26b3217fae8d743e99e0030ec56ce089b69ad25c551b65343c |
| `frameworks/dpf/LICENSE` | selected product component | 9e5f1b3c610b9c2da5c313bf81d577a7d1acec686bdb0384edefa6df0f90cd94 |
| `frameworks/dpf/LICENSING.md` | selected product component | f80502802237f19a0ea85303a792281e0f9c533e86d23f8a6174d5c18bd70864 |
| `frameworks/dpf/NOTICE.md` | selected product component | 17a0eafe4c07c5a5f7d15f0682dc067071cd6660f738a2c26b4ae010602e9b6e |
| `frameworks/dpf/REPERTOIRE.yaml` | selected product component | f7ebd9be7a1d1d575fa6243c5b03fcb36e5e47dc59e529036b91d5d9bcee384c |
| `frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | selected product component | cc9056e958c0435ec33666291f6fa4bb207d5e307ae6b28213f134f74d92bef4 |
| `frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md` | selected product component | 5d2ff495c0a6fff809092c8e36c826ae3a6d94860cf58d63ef61a41feaeedd87 |
| `frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | selected product component | a7ab62df62afe22086165830d0c91bf04c43d07437431f7d6944c571894da5ac |
| `frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md` | selected product component | dbf0f86337d24dcb89d90faa38240991579b9fe6d1487120285c36126673efa9 |
| `frameworks/dpf/sdlc/0.1.0/SDLC_DPF.md` | selected product component | eb6e5b1e69ee8192fbcd73acf05bca3484ac2637f79abb810e63d06e3a25f7da |
| `frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | selected product component | 45c49096102c11c7ac1024e3b459f7b9e791c48613163af46f2d63cfdf579887 |
| `modules/coordination/CONTRACT.md` | selected product component | 66a8cad0e6839587d48025c8e0840ff83c37e1d6a7638f40bd0e034e9bcaeebd |
| `modules/coordination/GUIDANCE.md` | selected product component | d5acbd63700e18d162557e40529395d93df1a9d38e01b4ab626d0ae57df6b416 |
| `modules/coordination/api.py` | selected product component | 2df8fb261287a54744cfa92cbb9c958bc96114bdc2fa564a0d32999a6ee735ea |
| `modules/effects/CONTRACT.md` | selected product component | 38339720cde001c4af4af3eac242af2e8395f13dd2d7a156efc14644c4c8f44b |
| `modules/effects/GUIDANCE.md` | selected product component | e78f62ba5e09c4e9f52501807703d667af4eca53f3b98a85b1568064a249d237 |
| `modules/effects/api.py` | selected product component | 054142aaea6287187238cf97dcd1f9d3a852224d77360b6daa907a375155a3bf |
| `modules/effects/operations.py` | selected product component | ec2be5ef2b71b9836772ffc935a95724104e8b7f63ce2f5511035efd6ee699f6 |
| `modules/execution/CONTRACT.md` | selected product component | 1aabccabf4a4674080dce494918920466ebb4d14fe3fde14d3758405a0f09cee |
| `modules/execution/EXECUTION_BASIS.md` | selected product component | 9689e12f3a56beb96fd2621d4044536aa88e8232290eb097302c607579947fb9 |
| `modules/execution/api.py` | selected product component | 5f50847385764a116a0042465926b9ba5cfe45938d8de68a3bb680ec89ccc9b0 |
| `modules/execution/operations.py` | selected product component | af38d55cf76b4472977fa6d7369bfac6358e019cd6a0fc8155254123db7bd66e |
| `modules/execution/profiles.py` | selected product component | ee01627ed36b5543c5b8402602b1d372b32e5e71ea91b584918095b660ad9f92 |
| `modules/execution/work_basis.py` | selected product component | d96f29cf52f4474b99b572daa29be14e2367f0b5045c7fe0cb68dd0a4428e16b |
| `modules/formation/CONTRACT.md` | selected product component | 604d41cb8c9b80d299830f276411a02cc1f00ee441a67eaa5159451b41870ba8 |
| `modules/formation/DOMAIN_WORK.md` | selected product component | c44fbc414f33e754b5040e350e264bb947259608df443131bcecdb93c839151b |
| `modules/formation/api.py` | selected product component | c2ffb6dd62fa3fec34b6e06fb5ce369091653ea26778965b6ad342788f8f2bc1 |
| `modules/formation/execution_basis.py` | selected product component | 01b3ac1d646126ed42f13a7b21878f597603b7986a0959f89279056d8ad60440 |
| `modules/formation/operations.py` | selected product component | 2d32a3f45424d43e3fd29e8a217c10b882150ad23d11860a3ec42d8d27279573 |
| `modules/governance/CONTRACT.md` | selected product component | 93a666400239dcf6b9ccbcb8855032fc93e3ae5899ebc232a331461c87acf5b3 |
| `modules/governance/GUIDANCE.md` | selected product component | 2fa3e398a9b5aca4fc3f994d755df986f0b5df437e5fb505b9925f227de18a0b |
| `modules/governance/api.py` | selected product component | aa7fa47660da19204449452102ec8586a87ea1ab08b9e17514f8ea47815ca6ca |
| `modules/governance/operations.py` | selected product component | 8a28acc269b1c6ea82b86b990fd9560e7b2574a728643435b15d3c32e302927e |
| `modules/governance/responses.py` | selected product component | 11fc582eb81eb3d1df75c16b626c4e46b4da500c2375bd1626906a5b8680cd0c |
| `modules/interaction/CONTRACT.md` | selected product component | d149e12fd6a373551d09a9620933b8b5a40ecd555c89e4024cc72406dca19439 |
| `modules/interaction/HUMAN_INTERACTION.md` | selected product component | 45efc43466c9b6a209e0b5487a37393e931635c5bb68d1b315891fe180cc53b4 |
| `modules/interaction/api.py` | selected product component | 57c2ef8e1926c0f37a0c158b5eebef315c060b6aad94726eb7f3209fbd56a5a0 |
| `modules/interaction/preferences.py` | selected product component | de98c54aa3652bb5518442a6f8c174dfce7c8c3c0ccbd66c0b7f80eeb7356d99 |
| `modules/interaction/presentation.py` | selected product component | c4749c9cac50683383d29cbf85bd03339a32ea164ea5b901273d97398edadd49 |
| `modules/recovery/CONTRACT.md` | selected product component | f55a04c3c69375a350c7c0370e2af6e5aa0821b6d9321226c7a2ae7cd01b9a6f |
| `modules/recovery/api.py` | selected product component | 12cb724d22c89207fcf7fb183f3860a911fba8e7d8c06f01c6f072601ab755e5 |
| `modules/reliance/CONTRACT.md` | selected product component | 7458f8dd2d291a510ec20520dc454d890d80da0aae62b379bdaa5e74f2c42674 |
| `modules/reliance/RECEIVING_USE.md` | selected product component | 6432c5c41b4d68a17d23b4746da3bfb4e240cf139f6f4db39a75333c5be0288d |
| `modules/reliance/api.py` | selected product component | fc0b842468dc11dd5f5bb2ee902697e62294699de097354010602d95370d28a9 |
| `modules/reliance/assessment.py` | selected product component | 2d8a1086c0d5d31d2a61b50a99839bcd775fce0ea96fc49de021569d26c63562 |
| `modules/self_development/EXPERIENCE.md` | selected product component | 2d7d1520e1d75a76c55ca3271c8220f10482316a29d82d46354be9a271ee0ce0 |
| `modules/self_development/GUIDANCE.md` | selected product component | 38998e5c243c4a92c9d014ea193cc1b36fdbb6b9ad2a5486161fb902ea9b7586 |
| `modules/sources/CONTRACT.md` | selected product component | 95c7617b371a11756f84e3dc436be7c5e424e94781d395b97065173e2596704f |
| `modules/sources/GUIDANCE.md` | selected product component | ed368ed69c45ef05b069e09bb42be5e1e2f9a472246a17a69f5aa851b31d4cb9 |
| `modules/sources/REGISTRATION.md` | selected product component | 360a8dd83ac544db36e3ababc220a8b1083dbb3b79b0859bf8c78fbdd8a6ad8a |
| `modules/sources/api.py` | selected product component | 9baede73e20499df1ad3883e2da2e969f86dbe73232a58e450083e1ffd0a3850 |
| `modules/sources/repertoire.py` | selected product component | f229e8801612d4d402076dfc96d959c753355402859e553362c8292b54bb0ed3 |
| `project/README.md` | selected product component | c233a3b5f6ed55be53c08ee9a12470386f7704cf2beca437b98fd846e56214dc |
| `project/artifacts/.gitkeep` | selected product component | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `project/reference/.gitkeep` | selected product component | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `project/source/.gitkeep` | selected product component | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `source/external-dpf/.gitkeep` | selected product component | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `templates/BOUNDED_EXECUTION_PROFILE_TEMPLATE.md` | selected product component | a52d6043394c38aed93b42b7f629bf1c8fde36dd21abfaba837cb2b61c22d9e1 |
| `templates/DPF_CONTRIBUTION_RESOLUTION_TEMPLATE.yaml` | selected product component | fa57c7307b90e39c8e62887b8d5ccdf180983cf2ed69a752221650f6c1db3821 |
| `templates/DPF_REPERTOIRE_TEMPLATE.yaml` | selected product component | 79cd2d60af505cb0100346a553e2edfba738c2945c2bdfe6c1111cc9831a3ace |
| `templates/POST_INITIATIVE_LESSONS_REVIEW_TEMPLATE.md` | selected product component | 2132c0d8657d051467831648c571af6b4858c6e630c3f21fc9d79ef825a190da |
| `templates/RUNTIME_CAPABILITY_PROFILE_TEMPLATE.yaml` | selected product component | bf60c842e513c050d0ff436a9ff30129b5b76f049a0d4fdd6e17a1e5b66680d2 |
| `templates/STATE_INDEX_TEMPLATE.yaml` | selected product component | b8917fcd018b830585a338337e82f865060bbb11ab4211ca55ea4afa90ff41e7 |
| `tools/package/integrity.py` | selected product component | ffcafb5be9c72e9ead7db2c3c13eae8986306dd534d29c9732c94919e0f192bc |
| `tools/package/prepare.py` | selected product component | 8b6e5e8c9f255ab4367eb3d8c1eba044745a4f1694065e2693a47436ba4ce1a9 |
| `tools/package/verify_configuration.py` | selected product component | 96e8df954f0f7fdb2afbc60099d47c63e08ff902766d2adca1d5ca50f122e812 |
