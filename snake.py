import random
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))

# Buttons
#no= x,y,width and length
rock_button = pygame.Rect(100, 200, 125, 80)
paper_button = pygame.Rect(250, 200, 150, 80)
scissor_button = pygame.Rect(450, 200, 180, 80)

# Fonts
big_font = pygame.font.Font(None, 60)
font = pygame.font.Font(None, 40)

you = None
computer = None
result = ""

choices = ["rock", "paper", "scissor"]


def check(computer, you):

    if computer == you:
        return 0

    if computer == 2 and you == 1:
        return -1

    if computer == 0 and you == 2:
        return -1

    if computer == 1 and you == 0:
        return -1

    return 1


running = True

while running:

    # Check events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Rock
            if rock_button.collidepoint(event.pos):
                you = 0
                computer = random.randint(0, 2)

                score = check(computer, you)

                if score == 0:
                    result = "It's a draw"
                elif score == -1:
                    result = "You lose"
                else:
                    result = "You win!"

            # Paper
            elif paper_button.collidepoint(event.pos):
                you = 1
                computer = random.randint(0, 2)

                score = check(computer, you)

                if score == 0:
                    result = "It's a draw"
                elif score == -1:
                    result = "You lose"
                else:
                    result = "You win!"

            # Scissor
            elif scissor_button.collidepoint(event.pos):
                you = 2
                computer = random.randint(0, 2)

                score = check(computer, you)

                if score == 0:
                    result = "It's a draw"
                elif score == -1:
                    result = "You lose"
                else:
                    result = "You win!"

    # Background
    screen.fill((30, 30, 30))

    # Title
    title = big_font.render(
        "ROCK, PAPER, SCISSOR",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (190, 80))

    # Draw buttons
    pygame.draw.rect(screen, (100, 100, 100), rock_button)
    pygame.draw.rect(screen, (100, 100, 100), paper_button)
    pygame.draw.rect(screen, (100, 100, 100), scissor_button)

    # Button text
    rock_text = font.render("Rock", True, (255, 255, 255))
    paper_text = font.render("Paper", True, (255, 255, 255))
    scissor_text = font.render("Scissor", True, (255, 255, 255))

    screen.blit(rock_text, (rock_button.x + 30, rock_button.y + 25))
    screen.blit(paper_text, (paper_button.x + 35, paper_button.y + 25))
    screen.blit(scissor_text, (scissor_button.x + 35, scissor_button.y + 25))

    # Show choices and result
    if you is not None:

        you_text = font.render(
            "You: " + choices[you],
            True,
            (255, 255, 255)
        )

        computer_text = font.render(
            "Computer: " + choices[computer],
            True,
            (255, 255, 255)
        )

        result_text = font.render(
            result,
            True,
            (255, 255, 255)
        )

        screen.blit(you_text, (100, 350))
        screen.blit(computer_text, (100, 390))
        screen.blit(result_text, (500, 370))

    # Update window
    pygame.display.flip()


pygame.quit()