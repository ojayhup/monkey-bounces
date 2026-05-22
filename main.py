def on_b_pressed():
    animation.run_movement_animation(monkey,
        animation.animation_presets(animation.bounce_right),
        2000,
        False)
    scene.camera_follow_sprite(mySprite)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    animation.run_movement_animation(monkey,
        animation.animation_presets(animation.bounce_left),
        2000,
        False)
    scene.camera_follow_sprite(mySprite)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

mySprite: Sprite = None
monkey: Sprite = None
scene.set_background_color(2)
monkey = sprites.create(img("""
        . . . . f f f f f . . . . . . .
        . . . f e e e e e f . . . . . .
        . . f d d d d e e e f . . . . .
        . c d f d d f d e e f f . . . .
        . c d f d d f d e e d d f . . .
        c d e e d d d d e e b d c . . .
        c d d d d c d d e e b d c . f f
        c c c c c d d d e e f c . f e f
        . f d d d d d e e f f . . f e f
        . . f f f f f e e e e f . f e f
        . . . . f e e e e e e e f f e f
        . . . f e f f e f e e e e f f .
        . . . f e f f e f e e e e f . .
        . . . f d b f d b f f e f . . .
        . . . f d d c d d b b d f . . .
        . . . . f f f f f f f f f . . .
        """),
    SpriteKind.player)
game.splash("press A ")
controller.move_sprite(monkey)