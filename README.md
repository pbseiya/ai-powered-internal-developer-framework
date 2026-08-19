# AI-Powered Internal Developer Framework

Framework สำหรับพัฒนาและ deploy แอพพลิเคชันภายในองค์กร ด้วย AI-assisted workflows

## 🎯 วัตถุประสงค์

1. **ลด Shadow IT** — จูงใจให้ user deploy ในองค์กรแทนที่จะออกไปนอก (Vercel, Render, etc.)
2. **AI-First Development** — ใช้ LLM ช่วยทุกขั้นตอน: docs, code review, testing
3. **Knowledge Management** — ทุก project ต้องมี LLM Wiki ก่อน deploy
4. **Governance & Compliance** — ควบคุมคุณภาพ, security, และ audit trail
5. **Self-Service** — ใช้ง่ายเหมือน Vercel แต่อยู่บน k3s ขององค์กร

## 🏗️ Architecture Overview

```
Developer → Gitea Push → Gitea Actions (CI)
    ↓
Auto Doc Generation (LLM Wiki)
    ↓
KM Approval (SA/SME Review)
    ↓
Auto PR & Code Review (AI)
    ↓
ArgoCD (GitOps CD) → k3s Cluster
    ↓
MCP Server Auto-Register → AI Agents ใช้งานได้
```

## 🛠️ Tech Stack

| Layer | Tool | หน้าที่ |
|-------|------|---------|
| **Git** | Gitea | Self-hosted Git server |
| **CI** | Gitea Actions | Build, test, generate docs |
| **CD** | ArgoCD | GitOps deploy to k3s |
| **Orchestration** | k3s | Lightweight Kubernetes |
| **LLM Gateway** | LiteLLM | Cache, log, route LLM calls |
| **LLM** | Alibaba Qwen (Token Plan) | Generate docs, review code |
| **Router** | 9router | Round-robin API keys |
| **Observability** | Langfuse | LLM input/output logging |
| **Cache** | Redis | LLM response cache |
| **Secrets** | Vault | API keys, credentials |
| **Registry** | Harbor | Container images |
| **Ingress** | Traefik | Auto-routing, TLS |
| **Monitoring** | Prometheus + Grafana | Metrics, dashboards |

## 📚 LLM Wiki — Gatekeeper สำหรับ Deploy

**กฎ: ไม่มี Wiki = ไม่มี Deploy**

ทุก project ต้องมี LLM Wiki ที่ผ่านการ approve แล้ว:

```
project-wiki/
├── raw/              ← source material (code, design docs)
├── wiki/             ← AI-generated structured knowledge
│   ├── index.md
│   ├── architecture.md
│   ├── api-reference.md
│   ├── deployment-guide.md
│   └── troubleshooting.md
└── outputs/          ← reports, answers
```

**Workflow:**
1. Dev push code → Gitea Actions trigger
2. LLM (Qwen) อ่าน code → สร้าง wiki pages
3. SA/SME review → approve/reject
4. ถ้า approve → อนุญาต deploy
5. ถ้า reject → แจ้ง Dev แก้ไข

## 🤖 Auto PR & Code Review

AI ช่วย:
- สร้าง PR อัตโนมัติเมื่อมี code changes
- Review code quality, security, best practices
- แก้ trivial issues (formatting, unused imports)
- Merge อัตโนมัติถ้าผ่าน criteria

## 🔌 MCP Server — ทุก App ต้องมี

**MCP (Model Context Protocol)** = มาตรฐานให้ AI agent เรียกใช้ tools

ทุก app ที่ deploy ต้องมี MCP server:

```python
from fastmcp import FastMCP

mcp = FastMCP("my-app")

@mcp.tool()
def query_data(query: str) -> dict:
    """Query data from app"""
    pass

# Auto-register to MCP catalog on deploy
```

## 🔐 Governance Checklist

ก่อน deploy ต้องผ่าน:
- ✅ LLM Wiki ครบถ้วน (architecture, API, deployment guide)
- ✅ Security scan ผ่าน (Trivy, Snyk)
- ✅ MCP server registered
- ✅ Resource limits defined (CPU, memory)
- ✅ Network policies configured
- ✅ Secrets stored in Vault

## 💰 Alibaba Token Plan

**Models ที่รองรับ:**
- Qwen: qwen3.7-max, qwen3.7-plus, qwen3.6-plus, qwen3.6-flash
- DeepSeek: deepseek-v4-pro, deepseek-v4-flash, deepseek-v3.2
- Kimi: kimi-k2.7-code, kimi-k2.6, kimi-k2.5
- GLM: glm-5.2, glm-5.1, glm-5
- MiniMax: MiniMax-M2.5

**Pricing:**
- Standard: $30/seat → 25,000 credits/month
- Pro: $100/seat → 100,000 credits/month
- Max: $200/seat → 250,000 credits/month
- Shared pack: $700 → 625,000 credits

**Architecture:** 9router + LiteLLM round-robin สำหรับ 2 Premium seats ($400/month)

## 📅 Roadmap

**Phase 1 (Month 1-2): Foundation**
- [ ] Setup k3s cluster
- [ ] Deploy Gitea + Gitea Actions
- [ ] Deploy ArgoCD, Harbor, Traefik
- [ ] Deploy LiteLLM + Redis + Langfuse

**Phase 2 (Month 3-4): Automation**
- [ ] Integrate Alibaba Qwen API
- [ ] Build auto-doc generation pipeline
- [ ] Implement KM approval workflow
- [ ] Create MCP server template

**Phase 3 (Month 5-6): Polish**
- [ ] Build self-service portal
- [ ] Implement governance policies
- [ ] Onboard 3 pilot projects
- [ ] Training & documentation

## 👥 องค์ประชุม

| Role | หน้าที่ |
|------|---------|
| Maintenance (User) | Requirements, pilot testing, feedback |
| AI-Eng | LLM integration, auto-doc, MCP, auto PR |
| SA | Architecture review, wiki schema, templates |
| Dev | Workflow, templates, portal |
| Infra&Security | k3s, ArgoCD, Vault, RBAC, monitoring |

## 📁 โครงสร้าง Project

```
ai-powered-internal-developer-framework/
├── README.md                 ← ไฟล์นี้
├── docs/
│   ├── meeting-agenda.md     ← วาระการประชุม
│   ├── architecture.md       ← สถาปัตยกรรมโดยละเอียด
│   ├── llm-wiki-guide.md     ← คู่มือ LLM Wiki
│   ├── mcp-guide.md          ← คู่มือ MCP Server
│   └── backup/               ← ข้อมูลสำรอง (Alibaba pricing, etc.)
├── templates/
│   ├── project-template/     ← Template สำหรับ project ใหม่
│   ├── wiki-template/        ← Template สำหรับ LLM Wiki
│   └── mcp-template/         ← Template สำหรับ MCP Server
├── wiki/
│   └── framework-wiki/       ← LLM Wiki ของ framework เอง
└── scripts/
    ├── setup-k3s.sh          ← Script ติดตั้ง k3s
    ├── setup-gitea.sh        ← Script ติดตั้ง Gitea
    └── deploy-litellm.sh     ← Script deploy LiteLLM
```

## 🎯 Success Metrics

- **Developer Satisfaction** — survey หลังใช้ 1 เดือน
- **Deployment Time** — ลดจาก X ชั่วโมง → Y นาที
- **Documentation Coverage** — 100% ของ projects มี wiki
- **Shadow IT Reduction** — ลด external deployments 50% ใน 3 เดือน

---

**หมายเหตุ:** นี่คือ **framework** ที่ทีมต้องพัฒนาต่อยอด ไม่ใช่ platform สำเร็จรูป
