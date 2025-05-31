import streamlit as st
from PIL import Image

# Configurações iniciais da página
st.set_page_config(page_title="Portfólio | Lucas Luiz Borges", layout="wide")

# Título
st.title("👨‍💻 Lucas Luiz Borges")
st.markdown("### Dev in Progress ⚙️ | Code & Iron 💪")

# Adicionando uma sidebar com links para contato
with st.sidebar:
    st.image("bannerme.png", caption="Lucas Luiz Borges", width=255)
    st.markdown("### Contatos")
    st.write("💼 [LinkedIn](https://www.linkedin.com/in/lucas-borges-987088160/)")
    st.write("📂 [GitHub](https://github.com/Borges045)")
    st.write("🌐 [Site pessoal](https://seusite.com)")

# Seções
st.header("🚀 Sobre Mim")
st.write("""
Sou um desenvolvedor apaixonado por tecnologia, com domínio em HTML, CSS, JavaScript, Python e em constante evolução. 
Atualmente desenvolvendo um sistema de gestão estilo Trello, usando tecnologias modernas e armazenamento local,
Atuando tambem no desenvolvimento de um sistema de automação para uma mecanica local usando Java.
Também sou entusiasta do fisiculturismo, disciplina que carrego tanto na academia quanto na programação.
""")

st.header("🧠 Habilidades")
cols = st.columns(3)
cols[0].markdown("- HTML & CSS")
cols[0].markdown("- JavaScript")
cols[1].markdown("- Python")
cols[1].markdown("- Streamlit(Py)")
cols[2].markdown("- LocalStorage API")
cols[2].markdown("- Java WIP")

st.header("📂 Projetos em Destaque")

st.subheader("📌 OrdoFlow")
st.write("Um Trello customizado, criado com HTML, CSS, JS e LocalStorage.")
st.markdown("[🔗 Ver repositório](https://github.com/Borges045/Projeto-Mensal)")

st.subheader("📌 Cartelas de Bingo Bíblico (Phython)")
st.write("Criação de 200 cartelas com temas de alimentos bíblicos, automatizando conteúdo visual.")
st.markdown("[🔗 Ver projeto](https://canva.com/seu-projeto)")


st.header("💪 Fisiculturismo e Disciplina")
st.write("""
Treinos diarios é o principio para aplicar os princípios do fisiculturismo — consistência, rotina e evolução — ao meu trabalho com código.
Minha rotina é ajustada para manter a produtividade e o foco mesmo com desafios de sono noturnos.
""")

#adicionando um texto interativo para enviar ususarios para os links
st.header("📬 Entre em Contato")
st.write("Caso tenha se interecado em minhas habilidades a sua esquerda tem uma barra com links de contatos.")

st.markdown("---")
st.markdown("Feito com ❤️ por Lucas Luiz Borges")
