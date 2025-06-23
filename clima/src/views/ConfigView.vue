<template>
  <div>
    <div class="config-view">
      <NavBar />
      <div class="config-container">
        <div class="title-box">
          <h1>Alterar Região</h1>
        </div>
        <hr style="width: 50%; border: 1px solid var(--w-primary)" />
        <div class="list-itens">
          <div
            class="form-check"
            v-for="(location, i) in locations"
            :key="`${i}-${location.value}`"
          >
            <input
              class="form-check-input"
              type="radio"
              name="location"
              :id="`radio-${location.value}`"
              :value="location.value"
              v-model="selectedLocation"
            />
            <label class="form-check-label" :for="`radio-${location.value}`">
              {{ location.label }}
            </label>
          </div>
        </div>
        <div class="button-box">
          <button class="btn btn-primary btn-color" @click="alterLocation">
            Slavar
          </button>
        </div>
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
  created() {
    const local = localStorage.getItem("location-selected");

    if (local) this.selectedLocation = local;

    return;
  },
  components: {
    NavBar,
    FooterItem,
  },
  data() {
    return {
      locations: [
        { label: "Criciúma", value: "Criciuma" },
        { label: "Içara", value: "Icara" },
        { label: "Cocal do Sul", value: "CocalDoSul" },
        { label: "Balneário Rincão", value: "BalnearioRincao" },
        { label: "Morro da Fumaça", value: "MorroDaFumaca" },
        { label: "Urussanga", value: "Urussanga" },
        { label: "Nova Veneza", value: "NovaVeneza" },
        { label: "Jaguaruna", value: "Jaguaruna" },
        { label: "Sangão", value: "Sangao" },
        { label: "Treviso", value: "Treviso" },
        { label: "Forquilhinha", value: "Forquilinha" },
        { label: "Araranguá", value: "Ararangua" },
        { label: "Tubarão", value: "Tubarao" },
      ],
      selectedLocation: "Criciuma",
    };
  },
  methods: {
    alterLocation() {
      localStorage.setItem("location-selected", this.selectedLocation);
      alert("Localização alterada");
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
h1 {
  margin: 0;
}

.form-check-input:checked {
  background-color: var(--w-primary);
  border-color: var(--w-primary);
}

.title-box {
  width: 50%;
  display: flex;
}

.button-box {
  width: 50%;
  display: flex;
  justify-content: flex-end;
}

.config-view {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.config-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.list-itens {
  width: 50%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  padding: 7px 14px;

  color: var(--w-primary);
}

.btn-color {
  background-color: var(--w-primary) !important;
  color: #fff;
  border: 1px solid var(--w-primary) !important;
  box-shadow: #0000003d 0px 3px 8px;
}

.btn-color:hover,
.btn-color:focus {
  background-color: var(--w-secondary) !important;
  border-color: var(--w-secondary) !important;
  color: #fff;
}

.btn-color:active,
.btn-color:disabled {
  background-color: var(--w-secondary) !important;
  border-color: var(--w-secondary) !important;
  color: #fff !important;
  box-shadow: none !important;
}
</style>
