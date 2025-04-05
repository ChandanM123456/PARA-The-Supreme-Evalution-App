document.getElementById("loginForm").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const email = document.getElementById("loginEmail").value.trim();
    const password = document.getElementById("loginPassword").value.trim();
  
    let users = JSON.parse(localStorage.getItem("paraUsers")) || [];
  
    const validUser = users.find(user => user.email === email && user.password === password);
  
    if (validUser) {
      localStorage.setItem("currentUser", JSON.stringify(validUser));
      document.getElementById("loginMsg").textContent = "Login successful! Welcome " + validUser.name;
      
      // Optionally redirect to dashboard
      // setTimeout(() => window.location.href = "dashboard.html", 1500);
    } else {
      document.getElementById("loginMsg").textContent = "Invalid email or password!";
    }
  });
  