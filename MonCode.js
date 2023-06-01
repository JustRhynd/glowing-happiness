rainbowText({
  selector: '.letters-wave',  // css selector of word container
  minSize: 48,                // in pixels
  maxSize: 72,                // in pixels
  align: 'flex-end',          // align items for letters in flexbox
  rainbow: true,              // enables hue change
  speed: 0.5,                   // 1 is 2PI in rad., 0.5 is PI in rad. etc
  rainbowSpeed: 0.5,            // speed of hue color change,
  frequency: -1.5          // frequency of sine
});


rainbowText({
  selector: '.rainbow',
  rainbow: true,
  rainbowSpeed: 0.4,
  frequency: 0.5
});

function rainbowText({ minSize, maxSize, selector, align, rainbow, speed, rainbowSpeed, frequency }) {
  const wordContainer = document.querySelectorAll(selector)

  for (let i of wordContainer) {
      const word = i.innerHTML
      i.style.alignItems = align
  
      const spanify = word => {
          let HTMLString = ''
          word.split('').forEach(l => {
          l === ' ' ?
              HTMLString += `<span>&nbsp;</span>` :
              HTMLString += `<span>${l}</span>`
          })
          return HTMLString
      }
  
      i.innerHTML = spanify(word)
  
      const letters = [].slice.call(i.querySelectorAll("span"))
      // letters.resverse()
  
      const loop = ms => {
          requestAnimationFrame(loop)
          letters.slice().reverse().forEach((l, i) => {
              let fontSize = parseInt(Math.sin(ms/(360 * speed) + (i/frequency)) * (maxSize - minSize) + maxSize, 10)
              l.style.fontSize = `${fontSize}px`
              if (rainbow) {
                  l.style.color = `hsl(${ms/(1/rainbowSpeed)+i*20}, 50%, 50%)`
                  l.style.textShadow = ` 0 0 12px hsl(${ms/(1/rainbowSpeed)+i*20}, 50%, 50%)`
              }
          });
      }
  
      loop(0);
  }
}
