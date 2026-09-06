# Instantiatio EWR — Closed Beta

| Field | Value |
|---|---|
| Package ID | `iEWR-5.0.1-beta` |
| Version | `5.0.1-beta` |
| Source baseline | `iEWR-closed-beta-2026-09-05` — accepted Closed Beta |
| Bundled DPF baseline | `iEWR-bundled-dpf-2026-09-06` — direct Human acceptance for local Closed Beta |
| Package status | Local Closed Beta 5.0.1-beta with accepted Bundled DPF Baseline; stated evidence limits preserved |
| distribution_ready | `false` |
| Public release | `not a public release` |
| Architecture contract | `1.0 RC — status preserved` |
| Clean baseline ZIP SHA-256 | `45da492fd342dab6764a3b4a65229618ac806c0d7342d02e77f541430f19ea67` |

87 selected components (86 hashed rows plus this self-unhashed manifest).
Five upstream Engineering DPFs use the exact 2026-09-05 editions from commit
`43c46859c3926a371fa60cfb1c76aefa19f9eaf9`: SYSE/ME/OCE/PSD refreshed, OPS added.
Experimental local SDLC, Core Contract and functional owner Python are unchanged.
The stable maintainer guide and empty external-DPF source scaffold are included.
One directly authorized P adapter change accepts the new source read root;
the project repertoire write target and existing path controls are preserved.
Other changes are limited to package profiles and necessary documentation/metadata.
This package does not create semantic Admission, publication or active-root cutover.
Current scope, test evidence limits and known gaps: BASELINE_STATUS.md.

Developer tests, fixtures and history are external to this inventory. Their
presence under the excluded project development contour does not expand the product or grant
authority. Source distribution readiness remains independently unresolved.

## Exact file inventory

Manifest self-unhashed; its SHA-256 is recorded outside the ZIP.

| Path | Role | SHA-256 |
|---|---|---|
| `AGENTS.md` | selected product component | 30CEAFE8F1F2D8DF994DF66E5059EBAD85A9A370CD67053CEDC48F620699AC48 |
| `BASELINE_STATUS.md` | selected product component | 5F5A5F5F6621F22458122624FEE0A68FAE4842C91DE2F1F9F5E17B82EAB92F77 |
| `ENGINEERING_WORK_BOOTSTRAP_GUIDE.md` | selected product component | 3105D704E1AF6F5FA824D24B6B9347B18FEC7E21A1FE71F1666CA1FAD5E27999 |
| `LICENSE` | selected product component | EF4DA070E506CD1018F449FC78BAE57537B96F797264CF56F133E411B5B611EC |
| `MODEL_SELECTION_RECOMMENDATIONS.md` | selected product component | B7059B78FD8A6D90E677520FBAF880CE6EF0634855E597D56847F590FEC43490 |
| `README.md` | selected product component | 57844AB309701E2AEF61432696EC78511A3729714193F516E180D81F0B60C2B1 |
| `WORKING_PROCESS_AND_LOOPS_GUIDE.md` | selected product component | 60F642AE1EB19A05669A7F0C86E6BA65A0E47F186718DF41C85CF6FCE097F557 |
| `adapters/ADAPTERS.md` | selected product component | 97A1C96747E2911878A03928E24C508BBB956E6FE0EDB450A43A35DF12FE396D |
| `adapters/agent_host/channel.py` | selected product component | 115D747D2DBB037CF2E6F1A912CCB939D5C347343EB47D92DB8E751A478F0390 |
| `adapters/agent_host/responses.py` | selected product component | 6DC5CA67A3F081248C6717E512DC87B87D3F7F2DD6CB0A997354FAD2889323DD |
| `adapters/filesystem/artifacts.py` | selected product component | 635A03A3784356241FF20087DBE8E9343CF75EB8EDCD285C609E9F4FC3240A23 |
| `adapters/filesystem/local.py` | selected product component | C571A45B534B51A68C45A9CEADFBD2F3613491879197EAA30E62894513AF34D2 |
| `adapters/filesystem/recovery.py` | selected product component | 9112729BB1F4B7ABD219F9F4D0A77300AC6AE3986C8593B8E379625D92A31BA6 |
| `adapters/filesystem/repertoire.py` | selected product component | 025559C5CFCCCF766C37BD4B198DBFF21D7CE6D558780FA6C6636F43A50B5D43 |
| `adapters/filesystem/repertoire_engine.py` | selected product component | 21BDDE5B57E80544B49EA588CA246099955AFCD71B9525BC3135A0652ECE53FD |
| `adapters/presentation/text.py` | selected product component | 84442E0AA5A586610717F5F66DCE9E91CC37D7E8969F2F8BFA9876B386D41415 |
| `app/bootstrap/CONFIGURATION.json` | selected product component | 0177B9A3D65A90E9543F08655E52ACF29EE53CD017B65EE1B1B90BD1583499FC |
| `app/bootstrap/ENTRY.md` | selected product component | 5F9851ED231C3235176C4E9EFC03D254D19B8D71E0284C7502B18137D2A1E224 |
| `app/bootstrap/operation.py` | selected product component | 6FDE3EA71CFCB8C9039C711713E60116BF56C9316370B50D91A61A9C056A0D5F |
| `catalog/README.md` | selected product component | 59E93386563B70B8A271D01EAD116F99E9455E0CE17BD59DDA4D5082E6E5B9E9 |
| `catalog/engineering_views/CATALOG.md` | selected product component | 04362CC56908A077C47D206A9064501C8285341E6285F38352A0760DB5A5AE34 |
| `catalog/engineering_views/README.md` | selected product component | 0576C71190C4EAC933529532D9A1CA9E91A435593CA50B1117F0E6F881099C00 |
| `catalog/engineering_views/templates/PROJECT_VIEW_PROFILE.yaml` | selected product component | 96A70940FA3A6D1AA0130481337ADA9B05573923F2797F7E9FF6DC2AE2B970B6 |
| `catalog/working_process_compositions/CATALOG.md` | selected product component | 35618F6DC9C84BF782321DAA6AB8E12794F4F3CB4A9C2D9102CD75757596C472 |
| `catalog/working_process_compositions/README.md` | selected product component | 6E2585504014BA917C4ACF7B39BD5C104FCB203A841F50B2E4805D5DB2B4CE76 |
| `catalog/working_process_compositions/templates/WORKING_PROCESS_COMPOSITION_RECORD.yaml` | selected product component | 4AE37EFC59297FC6D2700799EF484143F825C7C8E4C6A7B2F6879C9DA3BDD449 |
| `docs/BUNDLED_DPF_BASELINE_REFRESH_AND_INTEGRATION_GUIDE.md` | product maintainer guide | CECECA19C8AEDFF68EFC99344CB690609A20803F13B501C9946B45252B207B2F |
| `docs/DPF_FORMATION_METHOD.md` | selected product component | F5720BC446534877DA42FA63B5C7C30DE7E38110E8C7BBD17839735450BD8B52 |
| `docs/DPF_REGISTRATION_GUIDE.md` | selected product component | 0C6AE68196ED93D337BD492A93BC5B94832E41C780C45C28CE643151D91C6D48 |
| `docs/EWR_CORE_ARCHITECTURE_CONTRACT.md` | selected product component | EA9842606C82AF26B3217FAE8D743E99E0030EC56CE089B69AD25C551B65343C |
| `frameworks/dpf/REPERTOIRE.yaml` | selected product component | 1D6049A2BC08FC8B4BBF5504092C6452E722F09ECACA2CC13986B2467A571F11 |
| `frameworks/dpf/method-engineering/2026-09-05/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | selected product component | E0AF07CF45F2CE84B893202177DF2E429D09D6FE8AAC2FC78C38973141F04C81 |
| `frameworks/dpf/operations-management/2026-09-05/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md` | selected product component | 6B83575DFF6515A05406EA35AE17881BF47CAE39B915E1E1356D1DA34D12443B |
| `frameworks/dpf/organization-change-engineering/2026-09-05/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | selected product component | 423F20CA3EC01A36F08ABFC58C5392BAA7046B3DD40E127B8FAD7D5DE6FDF747 |
| `frameworks/dpf/problem-structuring-decision-support/2026-09-05/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md` | selected product component | 3A7EDDE17DB8301A44E0CBF8C9018B9DE8B343648FEF555532BDC01B561A219C |
| `frameworks/dpf/sdlc/0.1.0/SDLC_DPF.md` | selected product component | EB6E5B1E69EE8192FBCD73ACF05BCA3484AC2637F79ABB810E63D06E3A25F7DA |
| `frameworks/dpf/systems-engineering/2026-09-05/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | selected product component | CB5E2F3455CF18D2BD57C748FD7BADFBB027FD67EF3F877EC56A0C01BEA696E1 |
| `modules/coordination/CONTRACT.md` | selected product component | 66A8CAD0E6839587D48025C8E0840FF83C37E1D6A7638F40BD0E034E9BCAEEBD |
| `modules/coordination/GUIDANCE.md` | selected product component | D5ACBD63700E18D162557E40529395D93DF1A9D38E01B4AB626D0AE57DF6B416 |
| `modules/coordination/api.py` | selected product component | 2DF8FB261287A54744CFA92CBB9C958BC96114BDC2FA564A0D32999A6EE735EA |
| `modules/effects/CONTRACT.md` | selected product component | 38339720CDE001C4AF4AF3EAC242AF2E8395F13DD2D7A156EFC14644C4C8F44B |
| `modules/effects/GUIDANCE.md` | selected product component | E78F62BA5E09C4E9F52501807703D667AF4ECA53F3B98A85B1568064A249D237 |
| `modules/effects/api.py` | selected product component | 054142AAEA6287187238CF97DCD1F9D3A852224D77360B6DAA907A375155A3BF |
| `modules/effects/operations.py` | selected product component | EC2BE5EF2B71B9836772FFC935A95724104E8B7F63CE2F5511035EFD6EE699F6 |
| `modules/execution/CONTRACT.md` | selected product component | 1AABCCABF4A4674080DCE494918920466EBB4D14FE3FDE14D3758405A0F09CEE |
| `modules/execution/EXECUTION_BASIS.md` | selected product component | 9689E12F3A56BEB96FD2621D4044536AA88E8232290EB097302C607579947FB9 |
| `modules/execution/api.py` | selected product component | 5F50847385764A116A0042465926B9BA5CFE45938D8DE68A3BB680EC89CCC9B0 |
| `modules/execution/operations.py` | selected product component | AF38D55CF76B4472977FA6D7369BFAC6358E019CD6A0FC8155254123DB7BD66E |
| `modules/execution/profiles.py` | selected product component | EE01627ED36B5543C5B8402602B1D372B32E5E71EA91B584918095B660AD9F92 |
| `modules/execution/work_basis.py` | selected product component | D96F29CF52F4474B99B572DAA29BE14E2367F0B5045C7FE0CB68DD0A4428E16B |
| `modules/formation/CONTRACT.md` | selected product component | 604D41CB8C9B80D299830F276411A02CC1F00EE441A67EAA5159451B41870BA8 |
| `modules/formation/DOMAIN_WORK.md` | selected product component | C44FBC414F33E754B5040E350E264BB947259608DF443131BCECDB93C839151B |
| `modules/formation/api.py` | selected product component | C2FFB6DD62FA3FEC34B6E06FB5CE369091653EA26778965B6AD342788F8F2BC1 |
| `modules/formation/execution_basis.py` | selected product component | 01B3AC1D646126ED42F13A7B21878F597603B7986A0959F89279056D8AD60440 |
| `modules/formation/operations.py` | selected product component | 2D32A3F45424D43E3FD29E8A217C10B882150AD23D11860A3EC42D8D27279573 |
| `modules/governance/CONTRACT.md` | selected product component | 93A666400239DCF6B9CCBCB8855032FC93E3AE5899EBC232A331461C87ACF5B3 |
| `modules/governance/GUIDANCE.md` | selected product component | 2FA3E398A9B5ACA4FC3F994D755DF986F0B5DF437E5FB505B9925F227DE18A0B |
| `modules/governance/api.py` | selected product component | AA7FA47660DA19204449452102EC8586A87EA1AB08B9E17514F8EA47815CA6CA |
| `modules/governance/operations.py` | selected product component | 8A28ACC269B1C6EA82B86B990FD9560E7B2574A728643435B15D3C32E302927E |
| `modules/governance/responses.py` | selected product component | 11FC582EB81EB3D1DF75C16B626C4E46B4DA500C2375BD1626906A5B8680CD0C |
| `modules/interaction/CONTRACT.md` | selected product component | D149E12FD6A373551D09A9620933B8B5A40ECD555C89E4024CC72406DCA19439 |
| `modules/interaction/HUMAN_INTERACTION.md` | selected product component | 0A02B83FABEA5E807988B65E06A939201FA37B9462F80639E5007C740990F440 |
| `modules/interaction/api.py` | selected product component | 57C2EF8E1926C0F37A0C158B5EEBEF315C060B6AAD94726EB7F3209FBD56A5A0 |
| `modules/interaction/preferences.py` | selected product component | DE98C54AA3652BB5518442A6F8C174DFCE7C8C3C0CCBD66C0B7F80EEB7356D99 |
| `modules/interaction/presentation.py` | selected product component | 55F0329EB0B8753263DC3C528F7B3B098806F04EE6175E19FAFF19653885128E |
| `modules/recovery/CONTRACT.md` | selected product component | F55A04C3C69375A350C7C0370E2AF6E5AA0821B6D9321226C7A2AE7CD01B9A6F |
| `modules/recovery/api.py` | selected product component | 12CB724D22C89207FCF7FB183F3860A911FBA8E7D8C06F01C6F072601AB755E5 |
| `modules/reliance/CONTRACT.md` | selected product component | 7458F8DD2D291A510EC20520DC454D890D80DA0AAE62B379BDAA5E74F2C42674 |
| `modules/reliance/RECEIVING_USE.md` | selected product component | 6432C5C41B4D68A17D23B4746DA3BFB4E240CF139F6F4DB39A75333C5BE0288D |
| `modules/reliance/api.py` | selected product component | FC0B842468DC11DD5F5BB2EE902697E62294699DE097354010602D95370D28A9 |
| `modules/reliance/assessment.py` | selected product component | 2D8A1086C0D5D31D2A61B50A99839BCD775FCE0EA96FC49DE021569D26C63562 |
| `modules/sources/CONTRACT.md` | selected product component | 95C7617B371A11756F84E3DC436BE7C5E424E94781D395B97065173E2596704F |
| `modules/sources/GUIDANCE.md` | selected product component | ED368ED69C45EF05B069E09BB42BE5E1E2F9A472246A17A69F5AA851B31D4CB9 |
| `modules/sources/REGISTRATION.md` | selected product component | 360A8DD83AC544DB36E3ABABC220A8B1083DBB3B79B0859BF8C78FBDD8A6AD8A |
| `modules/sources/api.py` | selected product component | 9BAEDE73E20499DF1AD3883E2DA2E969F86DBE73232A58E450083E1FFD0A3850 |
| `modules/sources/repertoire.py` | selected product component | F229E8801612D4D402076DFC96D959C753355402859E553362C8292B54BB0ED3 |
| `project/artifacts/.gitkeep` | selected product component | 01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B |
| `source/external-dpf/.gitkeep` | empty external DPF source scaffold | E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855 |
| `templates/BOUNDED_EXECUTION_PROFILE_TEMPLATE.md` | selected product component | A52D6043394C38AED93B42B7F629BF1C8FDE36DD21ABFABA837CB2B61C22D9E1 |
| `templates/DPF_CONTRIBUTION_RESOLUTION_TEMPLATE.yaml` | selected product component | FA57C7307B90E39C8E62887B8D5CCDF180983CF2ED69A752221650F6C1DB3821 |
| `templates/DPF_REPERTOIRE_TEMPLATE.yaml` | selected product component | 79CD2D60AF505CB0100346A553E2EDFBA738C2945C2BDFE6C1111CC9831A3ACE |
| `templates/POST_INITIATIVE_LESSONS_REVIEW_TEMPLATE.md` | selected product component | 2132C0D8657D051467831648C571AF6B4858C6E630C3F21FC9D79EF825A190DA |
| `templates/RUNTIME_CAPABILITY_PROFILE_TEMPLATE.yaml` | selected product component | BF60C842E513C050D0FF436A9FF30129B5B76F049A0D4FDD6E17A1E5B66680D2 |
| `templates/STATE_INDEX_TEMPLATE.yaml` | selected product component | B8917FCD018B830585A338337E82F865060BBB11AB4211CA55EA4AFA90FF41E7 |
| `tools/package/integrity.py` | selected product component | 582C846E5369B1454625B2CE2732B64AB61CABB86E640A3E57D1CC90FE29EB92 |
| `tools/package/verify_configuration.py` | selected product component | BF172E52BD38D53074047DD80B6313224D65510CB70C11335D7C8F7E3AF44400 |
