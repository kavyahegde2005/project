function showSpecial() {
  const specials = [
    "Red Sause Pasta",
    "Hazelnut Cappuccino",
    "Hot Chocolate Mug",
    "Classic Iced Latte",
    "Mocha Espresso"
  ];
  const randomSpecial = specials[Math.floor(Math.random() * specials.length)];
  document.getElementById("special").textContent = `Today's Special: ${randomSpecial}`;
}
