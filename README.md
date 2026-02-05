Snake Game Using Python and Django

This project is a simple *Snake Game* developed using *Python and Django* for learning and practice purposes. The game runs in a web browser and demonstrates how Django can be used to serve a game interface while the core game logic is handled on the frontend using *HTML, CSS, and JavaScript*.

The objective of the game is to control the snake using the keyboard arrow keys, eat food to increase the snake’s length and score, and avoid collisions with the walls or the snake’s own body. The game responds to real-time keyboard input and ends when a collision occurs.

## Project Structure and Technologies

### Backend (Django)
Django is responsible for managing the project structure, handling URL routing, and rendering templates. It serves the frontend files to the browser while the game logic remains on the client side.

### Frontend (HTML, CSS, JavaScript)
The frontend consists of a single HTML page where the game canvas is displayed.
- *HTML* is used to structure the game interface  
- *CSS* provides basic styling  
- *JavaScript* handles snake movement, collision detection, food generation, score updates, and game-over logic  

## How to Run the Project

1. Install Django on your system.
2. Navigate to the project directory.
3. Apply database migrations.
4. Start the Django development server.
5. Open the local server address in a web browser to play the game.

The game starts automatically when the page loads and can be controlled using the keyboard arrow keys.

## Learning Outcomes

This project is intended for beginners who want to understand how *Python and Django integrate with frontend technologies*. It helps in learning:
- Django project structure
- URL routing
- Template rendering
- Integrating JavaScript-based game logic within a Django application

## Future Enhancements

The project can be extended with additional features such as:
- Difficulty levels
- Restart and pause functionality
- High score saving
- Animations and sound effects
