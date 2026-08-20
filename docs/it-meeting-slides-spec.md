# IT Internal Meeting Slides — Specification & Checklist

**ไฟล์นี้ใช้ตรวจสอบว่าสไลด์ที่ทำตรงตาม spec ที่ตกลงกัน**
**สร้าง:** สิงหาคม 2026
**เวอร์ชั่น:** v2 (IT Internal — กระชับ)

---

## 🎯 วัตถุประสงค์หลัก (ต้องปรากฏในสไลด์)

### Core Problem (ต้องสื่อให้ชัด)
- [ ] Maintenance = Developer ที่พัฒนา app เอง
- [ ] Pain point: ต้องส่ง code ให้ IT deploy → รอ 1-3 วัน
- [ ] Pain point: IT สั่งให้แก้ config, environment → วุ่นวาย
- [ ] เปรียบเทียบกับ Vercel/Render/Cloudflare/NeonDB/Supabase ที่ zero config

### Solution (ต้องสื่อให้ชัด)
- [ ] Self-service deployment — Maintenance deploy เองได้ ไม่ต้องรอ IT
- [ ] Zero config experience — ใช้ง่ายเหมือน Vercel/Render (push → deploy)
- [ ] On-premise only — ไม่เอา code/data ไปวางนอกองค์กร
- [ ] AI-powered — LLM ช่วยเขียนโค้ด, สร้าง docs, review code
- [ ] Data privacy control — ใช้ LLM ภายในองค์กร (Alibaba Qwen via LiteLLM)

### Key Principles (ต้องสะท้อนในทุก slide)
- [ ] Maintenance = Developer, IT = Enabler (ไม่ใช่ gatekeeper)
- [ ] Zero config — ไม่ต้อง config infrastructure เอง
- [ ] On-premise first — ควบคุม data privacy ได้ 100%
- [ ] AI-assisted — LLM ช่วยทุกขั้นตอน
- [ ] Self-service — Deploy, database, secrets ทำเองได้ทันที

---

## 📊 สไลด์ Overview

| รายการ | ค่า |
|--------|-----|
| **จำนวน slides** | ~22 slides |
| **เวลา prezentasi** | ~60 นาที |
| **กลุ่มเป้าหมาย** | SA, AI-Eng, Dev, Infra&Security, Maintenance |
| **ภาษา** | ไทย + technical English |
| **โทน** | กระชับ, technical, action-oriented |

---

## 📋 โครงสร้างสไลด์ (ต้องครบทุกส่วน)

### ส่วนที่ 1: Problem Statement (3 slides)
- [ ] Slide 1: Title — AI-Powered Internal Developer Framework
- [ ] Slide 2: The Problem — Maintenance pain points (รอ IT deploy, config วุ่นวาย)
- [ ] Slide 3: Why Not Just Use Vercel/Render? — Data privacy, compliance, cost

### ส่วนที่ 2: Solution Overview (4 slides)
- [ ] Slide 4: Our Vision — "Vercel-like experience, but on-premise"
- [ ] Slide 5: Architecture Overview — Diagram: GitLab → CI/CD → LLM → ArgoCD → k8s
- [ ] Slide 6: Key Features — Self-service, zero config DB, AI-powered, data privacy, preview env
- [ ] Slide 7: Tech Stack — Table: GitLab, ArgoCD, k8s, PostgreSQL+pgvector, LiteLLM, Qwen, Vault

### ส่วนที่ 3: Team Responsibilities (8 slides) ⭐ **สำคัญที่สุด**
- [ ] Slide 8: Team Overview — IT = Enabler, Maintenance = Developer
- [ ] Slide 9: Maintenance Team — Role, responsibilities, pain points to solve, what IT must deliver
- [ ] Slide 10: SA Team — Role, must do, design tasks checklist
- [ ] Slide 11: AI-Eng Team — Role, must do, design tasks checklist
- [ ] Slide 12: Dev Team — Role, must do, design tasks checklist
- [ ] Slide 13: Infra&Security Team — Role, must do, design tasks checklist
- [ ] Slide 14: Team Collaboration Matrix — ใครรอใคร, ใครส่งให้ใคร
- [ ] Slide 15: RACI Matrix — R/A/C/I สำหรับแต่ละ activity

### ส่วนที่ 4: Implementation Roadmap (3 slides)
- [ ] Slide 16: Phase 1 (Month 1-2) — Foundation, pilot app, tasks by team
- [ ] Slide 17: Phase 2 (Month 3-6) — Scale 5-10 apps, DORA metrics
- [ ] Slide 18: Phase 3 (Month 7-12) — Optimize, innovation culture, ROI

### ส่วนที่ 5: Technical Challenges (2 slides)
- [ ] Slide 19: Challenge 1 — Zero Config Experience (ทำให้เหมือน Vercel)
- [ ] Slide 20: Challenge 2 — Data Privacy with LLM (on-premise LLM)

### ส่วนที่ 6: Next Steps (2 slides)
- [ ] Slide 21: Immediate Actions (สัปดาห์นี้) — Checklist สำหรับแต่ละทีม
- [ ] Slide 22: Meeting with User (สัปดาห์หน้า) — Goals, agenda

---

## 👥 Team Responsibilities Checklist (ต้องระบุชัดในทุก slide)

### Maintenance (Developer)
- [ ] Role: Developer ที่พัฒนา app เอง
- [ ] Responsibilities: พัฒนา app, push code, deploy เอง, ให้ feedback
- [ ] Pain points to solve: ไม่ต้องรอ IT, ไม่ต้อง config infra, ไม่ต้องส่ง ticket
- [ ] IT must deliver: Self-service deployment, zero config DB, auto secrets injection

### SA (Solution Architect)
- [ ] Role: ออกแบบ architecture, workflow, schema
- [ ] Design tasks:
  - [ ] Architecture diagram (high-level + detailed)
  - [ ] Wiki schema (markdown structure, metadata)
  - [ ] Approval workflow (state machine)
  - [ ] RBAC matrix (roles, permissions)

### AI-Eng
- [ ] Role: LLM integration, auto-doc generation, MCP
- [ ] Design tasks:
  - [ ] LLM integration architecture (LiteLLM config)
  - [ ] Wiki generation prompt engineering
  - [ ] MCP server specification
  - [ ] Auto PR review rules

### Dev
- [ ] Role: Implementation, templates, workflow
- [ ] Design tasks:
  - [ ] CI/CD pipeline templates (YAML)
  - [ ] Kubernetes manifest templates
  - [ ] Database provisioning workflow
  - [ ] Preview environment lifecycle

### Infra&Security
- [ ] Role: Infrastructure setup, security, monitoring
- [ ] Design tasks:
  - [ ] Kubernetes cluster design (nodes, namespaces)
  - [ ] Network topology (VLAN, firewall rules)
  - [ ] Vault integration architecture
  - [ ] Monitoring dashboard design

---

## 🎯 Success Criteria (ต้องวัดได้)

### DORA Metrics Target
- [ ] Deployment Frequency: 1/เดือน → 10/สัปดาห์ (40x)
- [ ] Lead Time: 3 วัน → 15 นาที (288x)
- [ ] MTTR: 4 ชม. → 15 นาที (16x)
- [ ] Change Failure Rate: 20% → <5% (4x)

### Business Metrics
- [ ] Cost Avoidance: ฿2.7M ใน 3 ปี
- [ ] Deployment Time: ลด 99% (3 วัน → 15 นาที)
- [ ] Shadow IT: ลด 80%
- [ ] Compliance: 30% → 95%+

### Key Outcome
- [ ] Maintenance deploy เองได้ 100% (ไม่ต้องรอ IT)
- [ ] Zero config experience (เหมือน Vercel)
- [ ] Data privacy 100% (on-premise)

---

## 🔍 Quality Checklist (ก่อนส่งมอบ)

### Content Quality
- [ ] วัตถุประสงค์หลักปรากฏชัดเจนใน 3 slides แรก
- [ ] เปรียบเทียบกับ Vercel/Render/NeonDB (zero config)
- [ ] Team responsibilities ชัดเจน (ใครทำอะไร, ต้องออกแบบอะไร)
- [ ] Design tasks checklist สำหรับแต่ละทีม
- [ ] Implementation roadmap มี timeline ชัดเจน
- [ ] Next steps มี action items สำหรับสัปดาห์นี้

### Visual Quality
- [ ] ใช้ Marp theme เดียวกับเวอร์ชั่นก่อนหน้า (purple gradient)
- [ ] มี tables สำหรับ tech stack, RACI matrix
- [ ] มี code blocks สำหรับ architecture diagram
- [ ] มี highlight boxes สำหรับ key points
- [ ] มี columns สำหรับ side-by-side comparison
- [ ] ใช้ emoji เพื่อให้อ่านง่าย

### Technical Accuracy
- [ ] Tech stack ถูกต้อง (GitLab, ArgoCD, k8s, PostgreSQL+pgvector, LiteLLM, Qwen, Vault)
- [ ] Architecture diagram ถูกต้อง
- [ ] Team responsibilities สอดคล้องกับความเป็นจริง
- [ ] Implementation roadmap เป็นไปได้จริง

---

## 📝 Notes

**สิ่งที่ต้องเน้นเป็นพิเศษ:**
1. **Maintenance = Developer** — IT เป็น enabler ไม่ใช่ gatekeeper
2. **Zero config** — เปรียบเทียบกับ Vercel/Render/NeonDB ตลอด
3. **On-premise** — ไม่เอา data ออกนอกองค์กร (data privacy)
4. **AI-powered** — LLM ช่วยทุกขั้นตอน (code, docs, review)
5. **Actionable** — ทุกทีมรู้ว่าต้องทำอะไร, ต้องออกแบบอะไร

**สิ่งที่ต้องหลีกเลี่ยง:**
- ❌ ไม่ใช้คำว่า "Shadow IT" (ใช้ "Self-driven Solutions" แทน)
- ❌ ไม่ทำให้ IT ดูเป็น gatekeeper
- ❌ ไม่เน้น ROI/business value มากเกินไป (เวอร์ชั่น user เน้น, เวอร์ชั่น IT เน้น technical)
- ❌ ไม่ใช้ slide เยอะเกินไป (target: 22 slides, ไม่ใช่ 100+)

---

## ✅ Sign-off

- [ ] Spec ผ่านการ review จาก user
- [ ] สไลด์ Marp สร้างเสร็จ
- [ ] สไลด์ตรงตาม spec ทุกข้อ
- [ ] พร้อมสำหรับ IT internal meeting
