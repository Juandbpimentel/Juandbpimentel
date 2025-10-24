import os
import urllib.request
import re

# Lista de todas as imagens do README com nomes descritivos
images = {
    # Linguagens
    "java.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-plain.svg",
    "kotlin.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/kotlin.png",
    "python.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/python.png",
    "typescript.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg",
    "javascript.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
    "cpp.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg",
    "c.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg",
    "godot.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/godot.png",
    
    # Frameworks
    "android.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/android.png",
    "spring-boot.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/spring_boot.png",
    "nodejs.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg",
    "express.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/express.png",
    "nestjs.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nestjs/nestjs-original.svg",
    "react.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg",
    "nextjs.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nextjs/nextjs-original.svg",
    "vuejs.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg",
    "vuetify.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/vuetify_js.png",
    "fastapi.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg",
    
    # Ferramentas
    "tailwind.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg",
    "bootstrap.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/bootstrap.png",
    "material-ui.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/material_ui.png",
    "ant-design.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/ant_design.png",
    "pandas.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/pandas.png",
    "scikit-learn.svg": "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg",
    "flyway.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/flyway.png",
    "junit.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/junit.png",
    "jest.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jest/jest-plain.svg",
    
    # Bancos de Dados
    "postgresql.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg",
    "mongodb.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg",
    "firebase.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/firebase.png",
    "gcp.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/gcp.png",
    "sqlite.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/sqlite.png",
    "sqlalchemy.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original-wordmark.svg",
    
    # DevOps/Cloud
    "docker.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg",
    "cicd.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/ci_cd.png",
    "github-actions.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/githubactions/githubactions-original.svg",
    
    # Colaboração
    "git.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg",
    "figma.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg",
    "trello.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/trello/trello-plain.svg",
    "jira.png": "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/jira.png",
    "notion.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/notion/notion-original.svg",
}

def download_images():
    """Baixa todas as imagens para assets/images"""
    os.makedirs("assets/images", exist_ok=True)
    
    print("📥 Baixando imagens...")
    for filename, url in images.items():
        try:
            filepath = f"assets/images/{filename}"
            urllib.request.urlretrieve(url, filepath)
            print(f"✅ {filename}")
        except Exception as e:
            print(f"❌ Erro ao baixar {filename}: {e}")
    
    # Move profilecape.png se existir
    if os.path.exists("icons/profilecape.png"):
        os.rename("icons/profilecape.png", "assets/images/profilecape.png")
        print("✅ profilecape.png movido")
    
    # Copia prismaLogo.svg
    if os.path.exists("icons/prismaLogo.svg"):
        import shutil
        shutil.copy("icons/prismaLogo.svg", "assets/images/prisma.svg")
        print("✅ prisma.svg copiado")

def update_readme():
    """Atualiza o README.md com os novos caminhos"""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Substitui os caminhos das imagens
    replacements = {
        "./icons/profilecape.png": "./assets/images/profilecape.png",
        "./icons/prismaLogo.svg": "./assets/images/prisma.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-plain.svg": "./assets/images/java.svg",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/kotlin.png": "./assets/images/kotlin.png",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/python.png": "./assets/images/python.png",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg": "./assets/images/typescript.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg": "./assets/images/javascript.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg": "./assets/images/cpp.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg": "./assets/images/c.svg",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/godot.png": "./assets/images/godot.png",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/android.png": "./assets/images/android.png",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/spring_boot.png": "./assets/images/spring-boot.png",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg": "./assets/images/nodejs.svg",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/express.png": "./assets/images/express.png",
        "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nestjs/nestjs-original.svg": "./assets/images/nestjs.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg": "./assets/images/react.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nextjs/nextjs-original.svg": "./assets/images/nextjs.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg": "./assets/images/vuejs.svg",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/vuetify_js.png": "./assets/images/vuetify.png",
        "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg": "./assets/images/fastapi.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg": "./assets/images/tailwind.svg",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/bootstrap.png": "./assets/images/bootstrap.png",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/material_ui.png": "./assets/images/material-ui.png",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/ant_design.png": "./assets/images/ant-design.png",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/pandas.png": "./assets/images/pandas.png",
        "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg": "./assets/images/scikit-learn.svg",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/flyway.png": "./assets/images/flyway.png",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/junit.png": "./assets/images/junit.png",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jest/jest-plain.svg": "./assets/images/jest.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg": "./assets/images/postgresql.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg": "./assets/images/mongodb.svg",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/firebase.png": "./assets/images/firebase.png",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/gcp.png": "./assets/images/gcp.png",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/sqlite.png": "./assets/images/sqlite.png",
        "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original-wordmark.svg": "./assets/images/sqlalchemy.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg": "./assets/images/docker.svg",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/ci_cd.png": "./assets/images/cicd.png",
        "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/githubactions/githubactions-original.svg": "./assets/images/github-actions.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg": "./assets/images/git.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg": "./assets/images/figma.svg",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/trello/trello-plain.svg": "./assets/images/trello.svg",
        "https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/jira.png": "./assets/images/jira.png",
        "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/notion/notion-original.svg": "./assets/images/notion.svg",
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("✅ README.md atualizado")

if __name__ == "__main__":
    print("🚀 Iniciando organização das imagens...")
    download_images()
    update_readme()
    print("\n✨ Concluído! Agora execute:")
    print("git add .")
    print('git commit -m "Organize README images in assets/images folder"')
    print("git push origin organize-readme-images")
