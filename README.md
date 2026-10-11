# UPC Physics

**v0.2.0 · MIT · Python 3.9+ · MATLAB 可选**

面向 University Physics Competition（UPC）的物理研究 skill：从题目、假设与模型，到可复现计算、证据核验和完整参赛论文。默认中文讨论、英文写作。这是独立的备赛工具，与赛事主办方无隶属或背书关系。

它是 AI 助手读取的工作方法与工具包，复制后即可使用，无需重新“训练”模型。可以按团队习惯指定讨论与写作语言。

内含六个按需加载的功能模块：审题、资料研究、物理建模、计算与实验、验证、论文写作。机制细节与开放设计两条路线按问题特点选择，可以组合。核心方法由 2021、2022、2023、2025 年题目与 16 篇论文的比较提炼，发布内容为方法摘要、原创流程、脚本及模板。

## 1. 分享与安装

### 推荐：Git clone 安装

在本 GitHub 仓库页面点击 **Code → HTTPS** 复制地址，将下面的 `REPOSITORY_URL` 替换为该地址。

macOS / Linux 终端：

```bash
mkdir -p ~/.codex/skills
git clone REPOSITORY_URL ~/.codex/skills/upc-physics
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE/.codex/skills" | Out-Null
git clone REPOSITORY_URL "$env:USERPROFILE/.codex/skills/upc-physics"
```

无需编译或安装 Python 依赖。需要已安装 Git；仅在运行附带脚本时才需要 Python。若目标目录中已有旧版本，先将它移到别处备份，再克隆；保留自己修改过的内容。若设置了 `CODEX_HOME`，请将目标位置换成该目录下的 `skills/upc-physics`。

安装后的入口应是：

```text
~/.codex/skills/upc-physics/SKILL.md
```

`~` 表示自己的用户主目录。重启 Codex 后新建会话，在研究项目目录中调用 `$upc-physics`。若没有被识别，直接给出实际路径并要求读取该目录的 `SKILL.md` 及其引用文件，仍可使用。六个功能模块随主技能加载，无需分别安装。

更新到仓库 `main` 分支的最新内容：

```bash
git -C ~/.codex/skills/upc-physics pull --ff-only
```

Windows 将路径替换为 `"$env:USERPROFILE/.codex/skills/upc-physics"`。如果自己做过修改导致更新被阻止，先处理本地修改。队内需要固定同一公开版本时，执行下面的命令，并替换仓库地址和目标目录；Windows 同样换用自己的安装路径：

```bash
git clone --branch v0.2.0 --depth 1 REPOSITORY_URL ~/.codex/skills/upc-physics
```

固定标签安装不会跟随 `main` 更新，后续升级应显式选择新版本标签。

### 离线分享：Release 压缩包

从本仓库的 GitHub Releases 下载 `upc-physics-v0.2.0.zip`，解压得到完整的 `upc-physics/` 文件夹，将其放入上述技能目录。保留全部文件，包括许可与来源说明，队员间可直接分享这个压缩包。

同版本的 `.skill` 文件与 `.zip` 内容相同，供接受该扩展名的工具导入。`SHA256SUMS` 用于核对下载文件。压缩包安装不包含 Git 历史，升级时下载新版本。GitHub 自动生成的 “Source code” 包解压后需将包含 `SKILL.md` 的目录命名为 `upc-physics`。

**在其他 AI 编程助手中：**按该产品的技能安装方式放置文件，或要求助手读取完整文件夹的入口。不同产品的自动发现方式不同，不能保证 `$upc-physics` 通用；完整执行需要助手能够读写本地文件并运行命令。

## 2. 环境与材料

| 项目 | 需要准备什么 |
| --- | --- |
| 技能核心 | 本包已包含流程、四年案例摘要、工具与模板；无需复制开发项目的 `example/`、`training/` 或安装全部第三方 skills |
| 当前研究 | 完整题面、当前比赛要求，以及已有模型、代码或数据；从零开始时只需先提供题面 |
| 附带 Python 工具 | Python **3.9+**，仅使用标准库，无额外 `pip` 依赖；实际仿真库按题目另行选择 |
| MATLAB / Simulink | 可选；选择它们时需自行安装、具备相应许可及所需工具箱，先检查环境再运行 |
| PDF、联网与排版 | 按任务提供读取、检索或编译工具；技能包不捆绑这些软件或服务 |

案例中的 `example/...` 和 `training/...` 是开发来源定位，不是运行依赖。只有核对原文、重新分析案例时才需要另行提供相应材料。第三方 skills 有则按需使用，缺失时继续使用内置流程；来源说明保留在 [third-party.md](references/third-party.md)。

## 3. 直接这样开始

**新题目：**

> 使用 $upc-physics。题面在 problem.pdf，研究成果保存到本项目目录。先解释题目要求、比较建模路线，明确假设，再推进可运行的基线模型、验证和论文。

**已有代码或数据：**

> 使用 $upc-physics。阅读 src/ 和 data/，检查方程、单位、边界条件、数值误差及结论证据，修复问题并更新研究状态。

**开始写论文：**

> 使用 $upc-physics。根据本项目的真实研究结果和图表，搭建论证结构并完成英文参赛论文；列出证据缺口，不补造结果或引用。

想使用 MATLAB 时追加：“优先使用 MATLAB，先检测可执行程序、版本与工具箱；如果当前不能运行，明确区分已写代码与已验证结果。”把示例中的路径换成自己的实际文件位置，也可以直接用自然语言指定任务。

有时间或算力限制时一并说明，例如：“先完成足以回答原题的基线，在少数代表工况检查关键近似，再决定是否扩展昂贵仿真。”需要反复讨论构思时说明这一偏好；关键方案已经确认后，助手应继续完成获授权的工作。

流程按需要在“审题 → 资料 → 建模 → 计算/实验 → 验证 → 写作”之间迭代，已有成果可以从中途进入。机制细节与开放设计两条路线可以组合，不固定对应 A/B 题。

## 4. 可选的工具自检

在解压后的 `upc-physics/` 目录打开终端，运行：

```text
python3 scripts/numerical_checks.py biquad --a1 -1.9 --a2 0.88
```

应返回 JSON，极点约为 `1.1` 与 `0.8`，`stable` 为 `false`。这是预设的不稳定示例，正常退出表示诊断工具成功运行。如果本机 Python 命令是 `python` 或 `py -3`，替换命令开头即可。

也可让助手调用 `scripts/init_project.py` 创建新的研究目录，再用 `scripts/audit_project.py` 检查交付材料。新建空项目得到 `ready=false` 属于正常情况；审计只检查材料结构与关联，不证明物理结论正确。详见 [研究项目约定](references/project-contract.md)。MATLAB 的可选检查见 [软件适配](references/software.md)。

审计中的 `integrity_ok` 表示文件与关联完整性，`status_findings` 列出未完成或未通过的登记项。保留失败试算时，文件可以齐全而 `ready` 仍为 false；不要删掉失败或放宽标准来获得通过。

## 5. 队内交接

共享同一版技能包，以及完整的研究项目文件夹：题面、研究状态、参数和来源、代码、真实数据、图表及稿件。文件间尽量使用项目内相对路径，代码不要依赖某位队员的个人目录。科学研究记录用于复现；本技能不要求保存 AI 使用记录或对话档案。

仿真与实测必须区分；论文只使用有依据的结果。核心案例方法仍来自 2021、2022、2023、2025 年材料，本版补充实际使用后的通用执行方法，未附独立练习的题目、数据或解答。保留题须明确授权后使用；其反馈一旦参与修订，后续同题只能作为回归检查。比赛要求以当届核实的规则为准。

附带 Python 工具已在 macOS 的独立解压目录用 Python 3.9 与 3.12 检查；Windows/Linux 尚未实机测试。附带基础 MATLAB 算例已在 macOS / R2026b 实机通过，其他产品与工具箱仍须按需核验。助手的模型和工具能力会影响研究效果，复制技能不保证获得相同结果。

## 6. 许可与来源

本仓库的原创 skill 文本、脚本、模板和文档采用 [MIT License](LICENSE)，允许使用、修改和再分发，须保留版权和许可声明。第三方原始作品及软件继续适用各自的许可，详见 [NOTICE.md](NOTICE.md) 和 [第三方来源](references/third-party.md)。

原始赛题与获奖论文 PDF、完整解答、个人研究数据和开发对话不随本仓库分发。案例摘要保留来源定位与核验边界；获奖论文中的报告值不能直接视为已独立复现的结果。使用时应自行核实当届比赛要求。

## 7. 维护与版本

版本变化见 [CHANGELOG.md](CHANGELOG.md)。附带脚本只需 Python 标准库。在源码仓库根目录运行：

```text
python3 -m unittest discover -s tests -p 'test_*.py'
python3 tools/build_release.py
```

构建使用 `release-files.txt` 的明确文件清单，输出到 `dist/`：版本化 `.zip`、`.skill`、`manifest.json` 与 `SHA256SUMS`。安装包只包含使用 skill 所需文件和许可说明；维护测试与构建工具通过源码仓库获取。后续维护步骤见 [MAINTAINING.md](MAINTAINING.md)。
