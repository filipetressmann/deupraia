import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  en: {
    translation: {
      "PROPER": "Safe for Bathing",
      "IMPROPER": "Unsafe",
      "last_updated": "Last updated on",
      "beach_name": "Beach name",
      "result": "Classification",
      "user_location": "You are here!"
    }
  },
  pt: {
    translation: {
      "PROPER": "Própria para banho",
      "IMPROPER": "Imprópria",
      "last_updated": "Última atualização em",
      "beach_name": "Nome da praia",
      "result": "Classificação",
      "user_location": "Você está aqui!"
    }
  }
};

i18n.use(initReactI18next).init({
  resources,
  lng: 'pt', // default language
  interpolation: { escapeValue: false }
});

export default i18n;