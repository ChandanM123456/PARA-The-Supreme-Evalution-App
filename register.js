document.getElementById("registerForm").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const name = document.getElementById("regName").value.trim();
    const email = document.getElementById("regEmail").value.trim();
    const password = document.getElementById("regPassword").value.trim();
  
    let users = JSON.parse(localStorage.getItem("paraUsers")) || [];
  
    const emailExists = users.find(user => user.email === email);
    if (emailExists) {
      document.getElementById("registerMsg").textContent = "Email already registered!";
      return;
    }
  
    users.push({ name, email, password });
    localStorage.setItem("paraUsers", JSON.stringify(users));
  
    document.getElementById("registerMsg").textContent = "Registration successful! You can now log in.";
    document.getElementById("registerForm").reset();
  });
  