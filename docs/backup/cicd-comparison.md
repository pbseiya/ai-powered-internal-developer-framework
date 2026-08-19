# CI/CD Comparison Matrix

**เปรียบเทียบเครื่องมือ CI/CD สำหรับองค์กร**

---

## Options

| Tool | จุดเด่น | เหมาะกับ |
|------|---------|----------|
| **Gitea Actions** ⭐ | Compatible กับ GitHub Actions syntax, self-hosted, เบา | ทีมที่คุ้นเคย GitHub Actions, ต้องการ self-hosted |
| **GitLab CI/CD** | ครบวงจร (SCM + CI + CD), self-hosted ได้ | องค์กรใหญ่, ต้องการ all-in-one |
| **Argo Workflows** | K8s-native, ดีสำหรับ ML/data pipelines | Kubernetes-based, complex workflows |
| **Tekton** | K8s-native, Cloud Native Computing Foundation | ต้องการ extensibility สูง |
| **Jenkins** | Plugin เยอะ, ยืดหยุ่นสูงสุด | Legacy, ต้องการ custom สูง (แต่ maintain ยาก) |

---

## Detailed Comparison

| Feature | Gitea Actions | GitLab CI | Argo Workflows | Tekton |
|---------|--------------|-----------|----------------|--------|
| **Self-hosted** | ✅ | ✅ | ✅ (K8s) | ✅ (K8s) |
| **GitHub Actions compatible** | ✅ | ❌ | ❌ | ❌ |
| **K8s-native** | ❌ | ❌ | ✅ | ✅ |
| **YAML syntax** | ✅ | ✅ | ✅ | ✅ |
| **Resource usage** | Low | High | Medium | Medium |
| **Learning curve** | Low | Medium | High | High |
| **Community** | Growing | Large | Large | Medium |
| **Plugin ecosystem** | Medium | Large | Medium | Medium |
| **UI/UX** | Good | Excellent | Good (K8s dashboard) | Basic |
| **Scalability** | Medium | High | High | High |

---

## Recommendation

### เลือก: **Gitea Actions**

**เหตุผล:**
1. **Self-hosted ในองค์กรได้** — ควบคุม data, ไม่มี vendor lock-in
2. **Syntax เหมือน GitHub Actions** — migrate ง่าย, ทีมคุ้นเคย
3. **เบา** — เหมาะกับ k3s, ใช้ resource น้อย
4. **ใช้ร่วมกับ ArgoCD (GitOps) ได้ดี** — แยก CI (Gitea Actions) และ CD (ArgoCD)
5. **Open source** — ไม่มี license cost

**ข้อเสีย:**
- Community เล็กกว่า GitHub/GitLab
- Plugin น้อยกว่า (แต่สามารถใช้ GitHub Actions ที่ compatible ได้)

---

## Alternative: GitLab CI/CD

**เลือก GitLab CI ถ้า:**
- ต้องการ all-in-one (SCM + CI + CD ในที่เดียว)
- องค์กรใหญ่, มีทีม DevOps เต็มเวลา
- ต้องการ features ขั้นสูงเช่น Auto DevOps, Security Scanning built-in

**ข้อเสีย:**
- ใช้ resource เยอะ (ไม่เหมาะกับ k3s)
- Learning curve สูงกว่า
- Complex setup

---

## Architecture with Gitea Actions

```
Developer → Gitea (Git) → Gitea Actions (CI)
                              ↓
                         Build & Test
                              ↓
                         Generate Docs (LLM Wiki)
                              ↓
                         Push to Harbor (Container Registry)
                              ↓
                         Update Git Repo (manifests)
                              ↓
                         ArgoCD (CD) → k3s Cluster
```

**แยก CI/CD ชัดเจน:**
- **CI (Gitea Actions):** Build, test, generate docs, push images
- **CD (ArgoCD):** Deploy manifests จาก Git → k3s (GitOps)

---

## Migration Path

### จาก GitHub Actions → Gitea Actions

1. **Syntax เหมือนกัน** — YAML format เดียวกัน
2. **Actions ที่ compatible** — ใช้ GitHub Actions ที่ open source ได้
3. **Self-hosted runners** — ติดตั้ง runner ในองค์กร
4. **Webhooks** — ตั้ง trigger จาก Gitea events

### ตัวอย่าง Workflow

```yaml
# .gitea/workflows/ci.yml
name: CI Pipeline
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build
        run: |
          npm install
          npm run build
      
      - name: Test
        run: npm test
      
      - name: Generate Docs
        run: |
          # Call LLM API to generate wiki
          curl -X POST http://litellm:4000/v1/chat/completions \
            -H "Content-Type: application/json" \
            -d '{"model": "qwen-plus", "messages": [...]}'
      
      - name: Push to Harbor
        run: |
          docker build -t harbor.example.com/myapp:${{ gitea.sha }} .
          docker push harbor.example.com/myapp:${{ gitea.sha }}
```

---

## Links

- [Gitea Actions Documentation](https://docs.gitea.io/en/usages/actions/overview/)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Argo Workflows](https://argoproj.github.io/workflows/)
- [Tekton](https://tekton.dev/)

---

**Last Updated:** August 2026
