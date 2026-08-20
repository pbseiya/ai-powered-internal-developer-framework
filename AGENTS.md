# AI-Powered Internal Developer Framework

## 🎯 Project Objectives (วัตถุประสงค์หลัก)

### Core Problem
**Maintenance team** เป็น developer ที่พัฒนา application เอง แต่มี pain point:
- ❌ ต้องส่ง code ให้ IT deploy → รอ 1-3 วัน
- ❌ IT สั่งให้แก้ config, environment, dependencies → วุ่นวาย
- ❌ ไม่มี self-service deployment
- ❌ เปรียบเทียบกับ Vercel/Render/Cloudflare/NeonDB/Supabase ที่ zero config, ใช้ง่าย

### Solution Goals
✅ **Self-Service Deployment** — Maintenance deploy เองได้ ไม่ต้องรอ IT
✅ **Zero Config** — ใช้ง่ายเหมือน Vercel/Render (push → deploy)
✅ **On-Premise Only** — ไม่เอา code/data ไปวางนอกองค์กร (data privacy)
✅ **AI-Powered** — มี LLM ช่วยเขียนโค้ด, สร้าง documentation, review code
✅ **Data Privacy Control** — ใช้ LLM ภายในองค์กร (Alibaba Qwen via LiteLLM)

### Key Principles
1. **Maintenance = Developer** — IT เป็น enabler, ไม่ใช่ gatekeeper
2. **Zero Config** — ไม่ต้อง config infrastructure เอง
3. **On-Premise First** — ทุกอย่างอยู่ในองค์กร ควบคุม data privacy ได้
4. **AI-Assisted** — LLM ช่วยทุกขั้นตอน (code, docs, review)
5. **Self-Service** — Deploy, database, secrets ทำเองได้ทันที

---

## 🏗️ Architecture Overview

```
💡 Maintenance Dev → 💻 Code → 🤖 Auto Test → 📚 AI Docs → ✅ Review → 🚀 Deploy
                     ↓           ↓              ↓          ↓          ↓
                   GitLab    GitLab CI/CD     LLM Wiki   SA/SME    ArgoCD
                   Push        (Pipeline)    (Qwen AI)   Review    → k8s
```

### Tech Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Git + CI | GitLab | Git server + CI/CD pipeline |
| CD | ArgoCD | GitOps deploy to k8s |
| Orchestration | Kubernetes | Container orchestration |
| Database | PostgreSQL + pgvector | AI embeddings, RAG |
| DB Operator | CloudNativePG | PostgreSQL automation |
| LLM Gateway | LiteLLM | Cache, log, route LLM calls |
| LLM | Alibaba Qwen | Token Plan (credit-based, on-premise) |
| Secrets | Vault | API keys, credentials |
| Registry | Harbor | Container images |
| Monitoring | Prometheus + Grafana | Metrics, dashboards |

---

## 👥 Team Responsibilities

### Maintenance (Developer)
- **Role:** Developer ที่พัฒนา application เอง
- **Responsibilities:**
  - พัฒนา application (factory, back office, innovation)
  - Push code ไป GitLab
  - Deploy เองผ่าน self-service platform
  - ให้ feedback, requirements
- **Pain Points to Solve:**
  - ไม่ต้องรอ IT deploy
  - ไม่ต้อง config infrastructure เอง
  - ไม่ต้องส่ง ticket ขอ database, secrets

### SA (Solution Architect)
- **Role:** ออกแบบ architecture, workflow, schema
- **Responsibilities:**
  - ออกแบบ system architecture
  - ออกแบบ wiki schema (LLM auto-doc structure)
  - ออกแบบ approval workflow
  - ออกแบบ RBAC model
  - ออกแบบ database schema

### AI-Eng
- **Role:** LLM integration, auto-doc generation, MCP
- **Responsibilities:**
  - Integrate Alibaba Qwen ผ่าน LiteLLM
  - สร้าง LLM wiki generator (code → documentation)
  - สร้าง MCP server template
  - สร้าง auto PR reviewer (AI code review)
  - Optimize LLM caching

### Dev
- **Role:** Implementation, templates, workflow
- **Responsibilities:**
  - สร้าง GitLab CI/CD templates
  - สร้าง Kubernetes manifests
  - สร้าง database provisioning scripts
  - สร้าง preview environment automation
  - Integrate Vault

### Infra&Security
- **Role:** Infrastructure setup, security, monitoring
- **Responsibilities:**
  - Setup Kubernetes cluster
  - Setup GitLab + GitLab Runner
  - Setup ArgoCD (GitOps)
  - Setup Vault (secrets management)
  - Setup Harbor (container registry)
  - Setup Prometheus + Grafana
  - Config network policies, RBAC

---

## 📅 Implementation Phases

### Phase 1: Foundation (Month 1-2)
- Setup infrastructure (k8s, GitLab, ArgoCD)
- Deploy pilot app แรก (Predictive Maintenance)
- วัด baseline metrics

### Phase 2: Scale (Month 3-6)
- เพิ่ม 5-10 apps
- วัด DORA metrics จริง
- Optimize resource usage

### Phase 3: Optimize (Month 7-12)
- Optimize resource + automation
- สร้าง innovation culture
- วัด ROI จริง

---

## 🎯 Success Metrics

### DORA Metrics Target
- **Deployment Frequency:** 1/เดือน → 10/สัปดาห์ (40x)
- **Lead Time:** 3 วัน → 15 นาที (288x)
- **MTTR:** 4 ชม. → 15 นาที (16x)
- **Change Failure Rate:** 20% → <5% (4x)

### Business Metrics
- **Cost Avoidance:** ฿2.7M ใน 3 ปี (ไม่ต้องซื้อ server ใหม่)
- **Deployment Time:** ลด 99% (3 วัน → 15 นาที)
- **Shadow IT:** ลด 80%
- **Compliance:** 30% → 95%+

---

## 🔒 Data Privacy & Security

### On-Premise LLM
- ใช้ Alibaba Qwen ผ่าน LiteLLM (ภายในองค์กร)
- ไม่ส่ง code/data ไปยัง external LLM providers
- ควบคุม data privacy ได้ 100%

### Security Controls
- Network policies (VLAN, firewall)
- RBAC (k8s, GitLab)
- Vault (secrets management)
- Audit trail (ทุก deployment)

---

## 📚 Documentation Standards

### Auto-Generated Documentation
- LLM สร้าง wiki อัตโนมัติจาก code
- อัพเดทเมื่อ code เปลี่ยน
- Version control + approval workflow

### Documentation Structure
```
docs/
├── architecture/
│   ├── system-overview.md
│   └── component-diagrams.md
├── api/
│   └── auto-generated from code
├── guides/
│   ├── deployment.md
│   └── troubleshooting.md
└── wiki/
    └── auto-generated from code + LLM
```

---

## 🚀 Quick Start

### For Maintenance Developers
1. พัฒนา application ตามปกติ
2. Push code ไป GitLab
3. GitLab CI/CD รัน auto test + AI docs
4. ArgoCD deploy ไป Kubernetes อัตโนมัติ
5. Application พร้อมใช้งาน

### For IT Teams
1. Setup infrastructure (k8s, GitLab, ArgoCD, Vault)
2. สร้าง CI/CD templates
3. สร้าง database provisioning scripts
4. Config monitoring + alerting
5. Support maintenance team

---

## 📖 References

- [Meeting Presentation](./slides/meeting-presentation.md)
- [Meeting Agenda](./docs/meeting-agenda.md)
- [README](./README.md)
