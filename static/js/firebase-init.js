// static/js/firebase-init.js

import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.6.4/firebase-app.js';
import { getAuth, RecaptchaVerifier, signInWithPhoneNumber } from 'https://www.gstatic.com/firebasejs/9.6.4/firebase-auth.js';

const firebaseConfig = {
  apiKey: "AIzaSyBXWcAw012oCBbnOVKktRA2w_G3tr5-AKY",
  authDomain: "YOUR_DOMAIN",
  projectId: "kisan-ai-14c95",
  ...
};
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth, RecaptchaVerifier, signInWithPhoneNumber };
