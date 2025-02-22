
  document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.toggle-details');

    buttons.forEach(button => {
      button.addEventListener('click', function () {
        const extraDetails = this.previousElementSibling;

        if (extraDetails.style.display === 'none' || extraDetails.style.display === '') {
          extraDetails.style.display = 'block';
          this.textContent = 'View Less';
        } else {
          extraDetails.style.display = 'none';
          this.textContent = 'View More';
        }
      });
    });
  });

  
    document.addEventListener("DOMContentLoaded", () => {

      const messageBox = document.getElementById("message-box");
      const videoBox = document.getElementById("video-box");
      const tributeSection = document.getElementById("tribute-video");
  
      const revealElements = () => {
        const sectionTop = tributeSection.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
  
        if (sectionTop < windowHeight - 100) {
          // Reveal the message box
          messageBox.classList.remove("d-none");
          messageBox.classList.add("visible");
  
          // Delay the video reveal
          setTimeout(() => {
            videoBox.classList.remove("d-none");
            videoBox.classList.add("visible");
          }, 2000);
        }
      };
  
      // Trigger animation on scroll
      window.addEventListener("scroll", revealElements);
    });


    document.addEventListener("DOMContentLoaded", function () {
        const elementsToAnimate = document.querySelectorAll(".milestone, .message-item");
    
        const handleScroll = () => {
            const windowBottom = window.innerHeight + window.scrollY;
    
            elementsToAnimate.forEach((el) => {
                const elementTop = el.getBoundingClientRect().top + window.scrollY;
                if (windowBottom > elementTop + 50) {
                    el.classList.add("visible");
                }
            });
        };
    
        window.addEventListener("scroll", handleScroll);
        handleScroll(); // Trigger on load for visible elements
    });

    

    
 

