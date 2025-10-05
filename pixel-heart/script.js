const colors = [
  ["white","white","pink","pink","pink","white","white","white","white","white","pink","pink","pink","white","white"],
  ["white","pink","pink","pink","pink","pink","pink","white","pink","pink","pink","pink","pink","pink","white"],
  ["white","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","white"],
  ["white","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","white"],
  ["white","white","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","white","white"],
  ["white","white","white","pink","pink","pink","pink","pink","pink","pink","pink","pink","white","white","white"],
  ["white","white","white","white","pink","pink","pink","pink","pink","pink","pink","white","white","white","white"],
  ["white","white","white","white","white","pink","pink","pink","pink","pink","white","white","white","white","white"],
  ["white","white","white","white","white","white","pink","pink","pink","white","white","white","white","white","white"],
  ["white","white","white","white","white","white","white","pink","white","white","white","white","white","white","white"],
  ["white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"],
  ["white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"],
  ["white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"],
  ["white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"],
  ["white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"]
];



const gridSize = colors.length;
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

function draw(scale = 24) {
  ctx.clearRect(0, 0, gridSize, gridSize);
  for (let y = 0; y < gridSize; y++) {
    for (let x = 0; x < gridSize; x++) {
      ctx.fillStyle = colors[y][x] === "white" ? "#ffffff" : colors[y][x];
      ctx.fillRect(x, y, 1, 1);
    }
  }
  canvas.style.width = gridSize * scale + "px";
  canvas.style.height = gridSize * scale + "px";
}

draw();
