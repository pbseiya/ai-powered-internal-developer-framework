---
marp: true
theme: default
paginate: true
header: AI-Powered Internal Developer Framework
footer: IT Internal Meeting | August 2026
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #f0f4ff 0%, #e8f0ff 50%, #f5f0ff 100%);
    color: #1a202c;
    font-size: 22px;
    padding: 40px 50px;
  }
  section.lead {
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }
  section.lead h1 {
    font-size: 2.8em;
    font-weight: bold;
    margin-bottom: 0.3em;
    color: #fff;
  }
  section.lead h2 {
    font-size: 1.4em;
    font-weight: normal;
    opacity: 0.95;
    color: #fff;
  }
  section.lead p, section.lead ul, section.lead ol {
    color: #fff !important;
  }
  section.lead header, section.lead footer {
    color: rgba(255,255,255,0.8) !important;
  }
  section.lead::after {
    color: rgba(255,255,255,0.8) !important;
  }
  h1 {
    color: #5b21b6;
    border-bottom: 3px solid #7c3aed;
    padding-bottom: 0.2em;
    margin-bottom: 0.3em;
    font-size: 1.3em;
    font-weight: 700;
  }
  h2 {
    color: #7c3aed;
    font-size: 1.1em;
    margin-bottom: 0.25em;
    font-weight: 600;
  }
  h3 {
    font-size: 1em;
    margin-bottom: 0.2em;
    color: #6d28d9;
  }
  p, ul, ol {
    margin-bottom: 0.2em;
    line-height: 1.25;
    color: #2d3748;
  }
  li {
    margin-bottom: 0.03em;
    color: #2d3748;
  }
  code {
    background: rgba(124, 58, 237, 0.1);
    color: #5b21b6;
    padding: 0.1em 0.3em;
    border-radius: 3px;
    font-size: 0.85em;
  }
  pre {
    background: #f7f7fb;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 0.3em;
    font-size: 0.65em;
    line-height: 1.15;
    margin-bottom: 0.2em;
    color: #1a202c;
  }
  pre code {
    padding: 0;
    color: #1a202c;
  }
  table {
    width: 100%;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 0.75em;
    border-collapse: separate;
    border-spacing: 0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
  }
  th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: #ffffff !important;
    padding: 0.3em 0.4em;
    font-weight: 600;
    text-align: left;
    border: none;
  }
  td {
    color: #2d3748 !important;
    background: #ffffff !important;
    padding: 0.25em 0.4em;
    border-top: 1px solid #e2e8f0;
    border-bottom: 1px solid #e2e8f0;
  }
  tr:nth-child(even) td {
    background: #f8f9ff !important;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.6em;
  }
  .highlight {
    background: rgba(124, 58, 237, 0.08);
    padding: 0.25em 0.4em;
    border-radius: 5px;
    border-left: 4px solid #7c3aed;
    color: #2d3748;
  }
  .compact ul {
    margin: 0;
    padding-left: 1.2em;
  }
  .compact li {
    margin-bottom: 0;
    line-height: 1.3;
  }
  .red-note {
    color: #dc2626;
    font-weight: 600;
    font-style: italic;
  }
  header, footer {
    color: #64748b !important;
    font-size: 14px;
  }
  header::after, footer::after {
    color: #64748b !important;
  }
  section::after {
    color: #64748b !important;
  }
---

<!-- _class: lead -->

# AI-Powered Internal Developer Framework

## IT Internal Planning Meeting

<p style="color: white; opacity: 0.9; font-size: 1.2em; margin-top: 0.5em;">สร้าง Self-Service Platform ที่ Maintenance Deploy เองได้</p>

<p style="color: white; opacity: 0.85; font-size: 1em; margin-top: 1em;">Zero Config • On-Premise • AI-Powered</p>

<p style="color: white; opacity: 0.8; font-size: 0.9em; margin-top: 2em;">สิงหาคม 2026</p>

---

# 🎯 The Problem: Maintenance = Developer

<div class="highlight">

**Maintenance พัฒนา app เอง แต่มี pain points:**

- ❌ ต้องส่ง code ให้ IT deploy → รอ 1-3 วัน
- ❌ IT สั่งให้แก้ config, environment → **มีขั้นตอนมาก**
- ❌ ไม่มี self-service deployment
- ❌ เปรียบเทียบกับ Vercel/Render/Cloudflare/NeonDB/Supabase ที่ zero config
- ❌ **งบประมาณในการพัฒนาไม่เพียงพอ**

**Quote จาก Maintenance:**
> "ถ้าเอาไป deploy บน Vercel เสร็จใน 5 นาที แต่ต้องรอ IT 3 วัน"

</div>

---

# 🎯 Objective

<div class="highlight">

**เป้าหมายหลัก:**

1. **ลดขั้นตอน** — จาก 10+ ขั้นตอน → 3 ขั้นตอน (Code → Push → Deploy)
2. **ลดเวลา** — จาก 3 วัน → 15 นาที
3. **ลดค่าใช้จ่าย** — ใช้ infrastructure ที่มีอยู่ให้คุ้มค่า
4. **เพิ่มประสิทธิภาพ** — Maintenance พัฒนาและ deploy ได้เอง 100%
5. **Data Privacy** — ควบคุม code และ data ภายในองค์กร

**KPIs:**
- Deployment Frequency: 10x/สัปดาห์
- Lead Time for Changes: < 15 นาที
- Change Failure Rate: < 5%

</div>

---

# 💎 Benefit

<div class="columns">
<div>

**สำหรับ Maintenance:**
- ✅ Deploy เองได้ ไม่ต้องรอ IT
- ✅ ทดสอบได้ทันที (Preview Environment)
- ✅ สร้าง database เองได้ (Self-service)
- ✅ AI ช่วยเขียนโค้ดและ docs
- ✅ ลดเวลา deploy 99% (3 วัน → 15 นาที)

**สำหรับ IT:**
- ✅ ลด ticket จาก Maintenance
- ✅ ควบคุม security และ compliance
- ✅ Audit trail ครบถ้วน
- ✅ ใช้ infrastructure ที่มีอยู่ให้คุ้มค่า

</div>
<div>

**สำหรับองค์กร:**
- ✅ ลด Shadow IT (80% → 0%)
- ✅ เพิ่ม innovation speed
- ✅ ควบคุม data privacy 100%
- ✅ Cost avoidance: ฿2.7M ใน 3 ปี
- ✅ ROI > 4,000%

**สำหรับ Developer Experience:**
- ✅ Zero config — ใช้ง่ายเหมือน Vercel
- ✅ Self-service — ทำเองได้ทันที
- ✅ AI-powered — LLM ช่วยทุกขั้นตอน

</div>
</div>

---

# 🤔 Why Not Just Use Vercel/Render?

<div class="columns">
<div>

**External Cloud Platforms:**
- ❌ **Data Privacy** — ไม่เอา code/data ออกนอกองค์กร
- ❌ **Compliance** — ต้องควบคุม audit trail
- ❌ **Cost** — ค่าใช้จ่ายต่อเดือนสูง
- ❌ **Control** — ควบคุม infrastructure ไม่ได้

</div>
<div>

**Our Solution:**
- ✅ **On-Premise** — ทุกอย่างอยู่ในองค์กร
- ✅ **Data Privacy** — ควบคุมได้ 100%
- ✅ **Zero Config** — ใช้ง่ายเหมือน Vercel
- ✅ **AI-Powered** — LLM ช่วยทุกขั้นตอน

</div>
</div>

---

# 🚀 Our Vision: "Vercel-like, but On-Premise"

<div class="highlight">

**สิ่งที่ Maintenance จะได้:**

- ✅ **Push code → Deploy อัตโนมัติ** (15 นาที)
- ✅ **Zero config** — ไม่ต้อง config infrastructure
- ✅ **Self-service database** — สร้างได้ทันที (เหมือน NeonDB)
- ✅ **AI-powered** — LLM ช่วยเขียนโค้ด, สร้าง docs, review code
- ✅ **Data privacy** — ใช้ LLM ภายในองค์กร (Alibaba Qwen)

**IT = Enabler, ไม่ใช่ Gatekeeper**

</div>

---

# 🏗️ Architecture Overview

```
💡 Maintenance Dev → 💻 Code → 🤖 Auto Test → 📚 AI Docs → ✅ Review → 🚀 Deploy
                     ↓           ↓              ↓          ↓          ↓
                   GitLab    GitLab CI/CD     LLM Wiki   SA/SME    ArgoCD
                   Push        (Pipeline)    (Qwen AI)   Review    → k8s
```

**Key Components:**
- **GitLab** — Git + CI/CD pipeline
- **ArgoCD** — GitOps deploy to k8s
- **Kubernetes** — Container orchestration
- **LiteLLM + Qwen** — On-premise LLM
- **Vault** — Secrets management

---

# 🎁 Key Features

<div class="columns">
<div class="compact">

**1. Self-Service Deployment**
- Push → Deploy (เหมือน Vercel)
- ไม่ต้องรอ IT

**2. Zero Config Database**
- สร้าง database อัตโนมัติ (เหมือน NeonDB)
- Auto connection strings

**3. Preview Environments**
- ทุก MR ได้ environment ของตัวเอง
- ทดสอบก่อน merge

</div>
<div class="compact">

**4. AI-Powered**
- LLM ช่วยเขียนโค้ด
- Auto-generate documentation
- Auto code review

**5. Data Privacy**
- ใช้ LLM ภายในองค์กร
- ควบคุม data 100%

**6. Governance**
- Audit trail ครบ
- ตรวจสอบได้

</div>
</div>

---

# 🛠️ Tech Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Git + CI | **GitLab** | Git server + CI/CD pipeline |
| CD | **ArgoCD** | GitOps deploy to k8s |
| Orchestration | **Kubernetes** | Container orchestration |
| Database | **PostgreSQL + pgvector** | AI embeddings, RAG |
| DB Operator | **CloudNativePG** | PostgreSQL automation |
| LLM Gateway | **LiteLLM** | Cache, log, route LLM calls |
| LLM | **Alibaba Qwen** | Token Plan (on-premise) |
| Secrets | **Vault** | API keys, credentials |
| Registry | **Harbor** | Container images |
| Monitoring | **Prometheus + Grafana** | Metrics, dashboards |

---

# 👥 Team Overview: IT = Enabler

<div class="highlight">

**หลักการ:**
- **Maintenance = Developer** — พัฒนา app เอง, deploy เอง
- **IT = Platform Provider** — สร้าง platform ที่ใช้ง่าย

**5 Teams:**
1. **Maintenance** — Developer ที่พัฒนา app เอง
2. **SA** — ออกแบบ architecture, workflow <span class="red-note">Review Function Spec</span>
3. **AI-Eng** — LLM integration, auto-doc <span class="red-note">Provide System, Module AI</span>
4. **Dev** — Implementation, templates <span class="red-note">Review Code for AI</span>
5. **Infra&Security** — Infrastructure setup, security <span class="red-note">Test security</span>

**Goal:** ทำให้ Maintenance deploy เองได้ 100% (ไม่ต้องรอ IT)

</div>

---

# 👨‍🔧 Maintenance Team (Developer)

<div class="columns">
<div>

**Role:** Developer ที่พัฒนา application เอง

**Responsibilities:**
- พัฒนา application (factory, back office, innovation)
- Push code ไป GitLab
- Deploy เองผ่าน self-service platform
- ให้ feedback, requirements

**Deliverables:**
- ส่งมอบ Requirement Spec
- ส่งมอบ Function Spec ตาม Template Document Digital

</div>
<div>

**Pain Points to Solve:**
- ❌ ไม่ต้องรอ IT deploy
- ❌ ไม่ต้อง config infrastructure เอง
- ❌ ไม่ต้องส่ง ticket ขอ database, secrets

**IT Must Deliver:**
- ✅ Self-service deployment (push → deploy)
- ✅ Zero config database (เหมือน NeonDB)
- ✅ Auto secrets injection (เหมือน Vercel)

</div>
</div>

---

# 🏗️ SA Team (Solution Architect)

<div class="columns">
<div>

**Role:** ออกแบบ architecture, workflow, schema

**Must Do:**
- ออกแบบ system architecture (GitLab → ArgoCD → k8s)
- ออกแบบ wiki schema (LLM auto-doc structure)
- ออกแบบ approval workflow (code review, wiki publish)
- ออกแบบ RBAC model (factory vs backoffice vs user apps)

**Review:**
- ✅ Review Requirement Spec
- ✅ Review Functional Spec
- ✅ Review Architecture Design
- ✅ Review Workflow Design

</div>
<div>

**Design Tasks:**
- [ ] Architecture diagram (high-level + detailed)
- [ ] Wiki schema (markdown structure, metadata)
- [ ] Approval workflow (state machine)
- [ ] RBAC matrix (roles, permissions)

**Deliverables:** Architecture docs, workflow diagrams, RBAC matrix

</div>
</div>

---

# 🤖 AI-Eng Team

<div class="columns">
<div>

**Role:** LLM integration, auto-doc generation, MCP

**Must Do:**
- Integrate Alibaba Qwen ผ่าน LiteLLM (on-premise)
- สร้าง LLM wiki generator (code → documentation)
- สร้าง MCP server template (ทุก app มี MCP)
- สร้าง auto PR reviewer (AI code review)
- Optimize LLM caching (ลด cost)

</div>
<div>

**Design Tasks:**
- [ ] LLM integration architecture (LiteLLM config)
- [ ] Wiki generation prompt engineering
- [ ] MCP server specification
- [ ] Auto PR review rules

**Deliverables:** LLM integration, wiki generator, MCP template, auto reviewer

</div>
</div>

---

# 💻 Dev Team

<div class="columns">
<div>

**Role:** Implementation, templates, workflow

**Must Do:**
- สร้าง GitLab CI/CD templates (pipeline as code)
- สร้าง Kubernetes manifests (deployment, service, ingress)
- สร้าง database provisioning scripts (CloudNativePG)
- สร้าง preview environment automation
- Integrate Vault (secrets management)

**Review:**
- ✅ Review Source Code
- ✅ Review CI/CD Pipeline
- ✅ Review Kubernetes Manifests

</div>
<div>

**Design Tasks:**
- [ ] CI/CD pipeline templates (YAML)
- [ ] Kubernetes manifest templates
- [ ] Database provisioning workflow
- [ ] Preview environment lifecycle

**Deliverables:** CI/CD templates, k8s manifests, DB provisioning scripts

</div>
</div>

---

# 🔒 Infra&Security Team

<div class="columns">
<div>

**Role:** Infrastructure setup, security, monitoring

**Must Do:**
- Setup Kubernetes cluster (ใช้ server ที่มีอยู่)
- Setup GitLab + GitLab Runner
- Setup ArgoCD (GitOps)
- Setup Vault (secrets management)
- Setup Harbor (container registry)
- Setup Prometheus + Grafana (monitoring)
- Config network policies, RBAC

</div>
<div>

**Design Tasks:**
- [ ] Kubernetes cluster design (nodes, namespaces)
- [ ] Network topology (VLAN, firewall rules)
- [ ] Vault integration architecture
- [ ] Monitoring dashboard design

**Deliverables:** k8s cluster, GitLab, ArgoCD, Vault, monitoring

</div>
</div>

---

# 🔄 Team Collaboration Matrix

**Collaboration Flow:**

| Team | ต้องรอจาก | ต้องส่งให้ |
|------|-----------|-----------|
| **Maintenance** | N/A | Requirement Spec + Functional Spec → SA |
| **SA** | Requirement Spec (Maintenance) | Architecture + Review Spec → AI-Eng, Dev, Infra |
| **AI-Eng** | Architecture (SA) | LLM integration + AI Module → Dev |
| **Dev** | Architecture (SA), Infra (Infra) | Templates + Source Code Review → Maintenance |
| **Infra** | Architecture (SA) | Infrastructure → Dev, AI-Eng |

**Critical Path:**
1. **Maintenance** → เตรียม Requirement & Functional Spec → ส่งให้ SA confirm
2. **SA** → Review Spec → ออกแบบ Architecture → ส่งให้ Dev, AI-Eng, Infra
3. **Infra** → Setup Infrastructure → ส่งให้ Dev, AI-Eng
4. **Dev** → สร้าง Templates → Review Source Code → ส่งให้ Maintenance

---

# 📊 RACI Matrix

| Activity | Maintenance | SA | AI-Eng | Dev | Infra |
|----------|-------------|----|----|-----|-------|
| Requirement & Functional Spec | **R/A** | C | I | I | I |
| Review Spec | C | **R/A** | C | C | C |
| Architecture design | C | **R/A** | C | C | C |
| LLM integration | I | C | **R/A** | C | I |
| k8s setup | I | C | I | C | **R/A** |
| CI/CD templates | C | I | I | **R/A** | C |
| Review Source Code | C | C | C | **R/A** | I |
| Test Security | R | C | C | C | **R/A** |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

# 📅 Phase 1: Foundation (Month 1-2)

<div class="highlight">

**Goals:**
- Setup infrastructure (k8s, GitLab, ArgoCD)
- Deploy pilot app แรก (Predictive Maintenance)
- **Maintenance deploy เองได้ (ไม่ต้องรอ IT)**

**Tasks by team:**
- **Maintenance:** เตรียม Requirement Spec + Functional Spec
- **SA:** Review Spec → ออกแบบ architecture, wiki schema
- **AI-Eng:** Integrate Qwen LLM, สร้าง wiki generator prototype
- **Dev:** สร้าง CI/CD templates, Kubernetes manifests
- **Infra:** Setup k8s cluster, GitLab, ArgoCD, Vault

**Review Milestones:**
- ✅ Review Requirement & Functional Spec (Week 1)
- ✅ Review Architecture Design (Week 2)
- ✅ Review Infrastructure Setup (Week 4)

**Deliverables:**
- ✅ k8s cluster running
- ✅ GitLab + ArgoCD configured
- ✅ Pilot app deployed โดย Maintenance
- ✅ Baseline metrics recorded

</div>

---

# 📅 Phase 2: Scale (Month 3-6)

<div class="highlight">

**Goals:**
- เพิ่ม 5-10 apps
- วัด DORA metrics จริง
- **Zero config database working**

**Tasks by team:**
- **SA:** Review Architecture → ออกแบบ approval workflow, RBAC
- **AI-Eng:** สร้าง MCP server template, auto PR reviewer
- **Dev:** Review Source Code → สร้าง database provisioning, preview environments
- **Infra:** Config network policies, monitoring dashboards
- **Maintenance:** ให้ feedback, ทดสอบระบบ

**Review Milestones:**
- ✅ Review Workflow & RBAC Design (Month 3)
- ✅ Review Database Provisioning (Month 4)
- ✅ Review Preview Environments (Month 5)
- ✅ Review Security & Compliance (Month 6)

**Deliverables:**
- ✅ 5-10 apps deployed โดย Maintenance
- ✅ DORA metrics improved (deployment time < 15 นาที)
- ✅ Auto-doc generation working
- ✅ Self-service database provisioning (เหมือน NeonDB)

</div>

---

# 📅 Phase 3: Optimize (Month 7-12)

<div class="highlight">

**Goals:**
- Optimize resource + automation
- สร้าง innovation culture
- **Maintenance deploy เองได้ 100%**

**Tasks by team:**
- **SA:** Review & Optimize architecture based on feedback
- **AI-Eng:** Optimize LLM caching, ลด cost
- **Dev:** Review & Optimize CI/CD pipelines, ลด build time
- **Infra:** Right-sizing resources, auto-scaling
- **Maintenance:** แชร์ success stories, เพิ่ม apps

**Review Milestones:**
- ✅ Review Performance Metrics (Month 8)
- ✅ Review Cost Optimization (Month 9)
- ✅ Review Automation Level (Month 10)
- ✅ Review ROI & Success Metrics (Month 12)

**Deliverables:**
- ✅ Resource utilization > 70%
- ✅ Deployment time < 15 นาที (เหมือน Vercel)
- ✅ Maintenance deploy เองได้ 100%
- ✅ ROI > 4,000%

</div>

---

# ⚠️ Challenge 1: Zero Config Experience

<div class="columns">
<div>

**ปัญหา:**
ทำให้ใช้ง่ายเหมือน Vercel/Render ยาก

**ความท้าทาย:**
- Auto-detect framework (Next.js, React, Node.js)
- Auto-config build settings
- Auto-inject environment variables
- Auto-provision database

</div>
<div>

**วิธีแก้:**
- ✅ สร้าง CI/CD templates ที่ auto-detect framework
- ✅ ใช้ CloudNativePG สำหรับ auto-provision database
- ✅ ใช้ Vault สำหรับ auto-inject secrets
- ✅ สร้าง preview environments อัตโนมัติ

**Target:** Push → Deploy ใน 15 นาที

</div>
</div>

---

# ⚠️ Challenge 2: Data Privacy with LLM

<div class="columns">
<div>

**ปัญหา:**
ต้องใช้ LLM แต่ไม่ส่ง data ออกนอกองค์กร

**ความท้าทาย:**
- Code อาจมี sensitive data
- Documentation อาจมีข้อมูลลับ
- ต้องควบคุม LLM calls 100%

</div>
<div>

**วิธีแก้:**
- ✅ ใช้ Alibaba Qwen ผ่าน LiteLLM (on-premise)
- ✅ LLM caching (ลด duplicate calls)
- ✅ Audit trail (ทุก LLM call)
- ✅ Network isolation (LLM อยู่ภายในองค์กร)

**Target:** Data privacy 100%

</div>
</div>

---

# 🎯 Immediate Actions (สัปดาห์นี้)

<div class="columns">
<div class="compact">

**SA:**
- [ ] Draft architecture diagram
- [ ] Draft wiki schema

**AI-Eng:**
- [ ] Setup LiteLLM + Qwen integration
- [ ] Test wiki generation prototype

**Dev:**
- [ ] Draft CI/CD pipeline templates
- [ ] Draft Kubernetes manifests

</div>
<div class="compact">

**Infra:**
- [ ] Inventory existing servers
- [ ] Draft k8s cluster design

**Maintenance:**
- [ ] List pain points (deployment, database, secrets)
- [ ] Select 2-3 pilot apps

**Goal:** พร้อมสำหรับ meeting กับ user สัปดาห์หน้า

</div>
</div>

---

# 📅 Meeting with User (สัปดาห์หน้า)

<div class="highlight">

**Goals:**
- Present framework to Maintenance
- Demo zero-config deployment (เปรียบเทียบกับ Vercel)
- Get feedback on requirements
- Confirm pilot projects

**Agenda (90 นาที):**
1. จุดเริ่มต้น: ไอเดียที่ดีสมควรได้รับการสนับสนุน (15 นาที)
2. Journey: จากไอเดียสู่ระบบจริง (20 นาที)
3. ทีมของเรา: ใครช่วยอะไรได้บ้าง (15 นาที)
4. AI ช่วยอะไรได้บ้าง (15 นาที)
5. เริ่มต้นอย่างไร (15 นาที)

**Expected Outcome:**
- ✅ Maintenance เห็นภาพและเข้าใจ
- ✅ Confirm pilot projects
- ✅ ตั้ง expectation ที่ตรงกัน

</div>

---

<!-- _class: lead -->

# 🎯 Summary

## IT = Enabler, Maintenance = Developer

<p style="color: white; opacity: 0.9; font-size: 1.2em; margin-top: 0.5em;">สร้าง Self-Service Platform ที่ Maintenance Deploy เองได้</p>

<p style="color: white; opacity: 0.85; font-size: 1em; margin-top: 1em;">Zero Config • On-Premise • AI-Powered • Data Privacy</p>

<p style="color: white; opacity: 0.8; font-size: 0.9em; margin-top: 2em;">เป้าหมาย: Maintenance deploy เองได้ 100% ใน 15 นาที</p>
