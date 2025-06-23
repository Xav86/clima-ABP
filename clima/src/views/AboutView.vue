<template>
  <div>
    <div class="about-view">
      <NavBar />
      <div class="about-body">
        <h1>Sobre o Projeto</h1>
        <p>
          Este projeto foi desenvolvido como parte da disciplina de Front-end do
          curso de Engenharia de Computação, com o objetivo de aplicar conceitos
          de Frameworks.
        </p>

        <h2>Objetivo</h2>
        <p>
          O principal objetivo deste sistema é criar um sistema que permita
          visualizar de forma facil a previsão do tempo. Ele foi pensado para os
          alunos da faculdade, onde em totens em pontos da faculdade permitiriam
          de forma facil qualquer aluno chegar o clima atual ou dos dias
          seguintes para qualquer fim.
        </p>

        <h2>Tecnologias Utilizadas</h2>
        <ul>
          <li>Vue.js</li>
          <li>Bootstrap</li>
          <li>Axios</li>
          <li>Moment</li>
          <li>Git & Github</li>
          <li>
            API de Clima:
            <a href="https://www.visualcrossing.com" target="_blank"
              >Visualcrossing</a
            >
          </li>
        </ul>

        <h2>Funcionalidades Principais</h2>
        <ul>
          <li>Exibição de clima atual com ícones e dados em tempo real</li>
          <li>Previsão dos próximos dias</li>
          <li>Modo dinâmico de dia/noite baseado na hora atual</li>
        </ul>

        <h2>Desenvolvedor(es)</h2>
        <ul>
          <li>Gustavo Gonçalves dos Santos</li>
          <li>Calebe Arlan Souza da Silva</li>
          <li>Lucas Pizoni Flores</li>
        </ul>

        <h2>Repositório</h2>
        <p>
          O código-fonte está disponível em:
          <a href="https://github.com/Xav86/clima-ABP" target="_blank"
            >GitHub</a
          >
        </p>
      </div>
    </div>
    <FooterItem />
  </div>
</template>

<script>
import FooterItem from "@/Components/FooterItem.vue";
import NavBar from "@/Components/NavBar/NavBar.vue";

export default {
  name: "AboutView",
  components: {
    NavBar,
    FooterItem,
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
}

.about-view {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.about-body {
  width: 50%;
  display: flex;
  flex-direction: column;

  padding-top: 20px;
  margin: 0 auto;

  text-align: center;
  color: var(--w-primary);
}
</style>
