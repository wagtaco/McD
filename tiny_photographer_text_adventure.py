"""Text adventure adaptation of "Aunt's Tiny Photographer" intro sequences.

This interactive fiction allows the player to experience Ian's terrifying
perspective during the early scenes (intro, table, cupcake) of the story.
"""
from __future__ import annotations

import sys
from textwrap import fill


def wrap(text: str) -> str:
    """Wrap text to 79 columns for consistent output."""
    return "\n".join(
        "" if not paragraph else fill(paragraph, width=79)
        for paragraph in text.splitlines()
    )


def prompt_choice(prompt: str, choices: dict[str, str]) -> str:
    """Prompt the player until a valid choice key is entered."""
    print(wrap(prompt))
    print()
    for key, description in choices.items():
        print(f"  [{key}] {description}")
    print()

    valid = set(choices)
    while True:
        response = input("> ").strip().lower()
        if response in valid:
            return response
        print(wrap("Your answer evaporates unheard in the cavernous air. Try again."))


def death(description: str) -> bool:
    """Describe the player's demise and ask whether to restart."""
    print()
    print(wrap(description))
    print()
    print(wrap("Your story ends in darkness."))
    while True:
        answer = input("Would you like to restart from the beginning? (y/n) ").strip().lower()
        if answer in {"y", "yes"}:
            print()
            return True
        if answer in {"n", "no"}:
            print(wrap("The silence swallows you forever."))
            sys.exit(0)
        print(wrap("The void does not understand. Answer yes or no."))


def remote_escape(prelude: str | None = None) -> None:
    """Deliver the closing escape sequence, optionally with a prelude."""
    if prelude:
        print(wrap(prelude))
        print()
    print(wrap(
        "You hurl yourself from the cupcake, landing hard on the table and rolling "
        "beneath the arch of her curling fingers. The remote looms nearby. You slam "
        "your palm on the minus key, praying you hit the right command. Katie gasps "
        "as the belt warms around your waist. The world jolts, then shrinks. Wood "
        "becomes manageable grain. Her hand, frozen mid-grab, now merely enormous "
        "instead of godlike."
    ))
    print()
    print(wrap(
        "Katie blinks, eyes clearing as though the spell breaks. She sets the "
        "cupcake down, horrified at the frosting-smeared wreck she made of you. Her "
        "whisper shakes. 'Ian? Are you okay?' You can only pant, camera clutched to "
        "your chest like a life raft. The night is far from over, but for now you "
        "are alive."
    ))
    print()
    print(wrap(
        "TO BE CONTINUED... The mountains of Katie's world still loom, but the next "
        "descent will have to wait."
    ))
    print()


def intro_scene() -> bool:
    print(wrap(
        "You breathe in the waxy perfume of old tools and dust as you stand in the "
        "garage, camera strap digging into your shoulder. Katie lounges opposite "
        "you with a sweating bottle of berry wine and a thousand-yard stare that "
        "slides off the concrete floor and lands on you like a fallen chandelier. "
        "You know this speech by heart—tell her she is beautiful, that the shrinking "
        "gigs help people reclaim themselves—but tonight your own words sound thin. "
        "Because you are the one handing a remote that can erase you to a woman who "
        "has been teetering between laughter and tears for months."))
    print()
    print(wrap(
        "Katie's fingers toy with the prototype belt you set across your lap. "
        "Her thumb hovers over the emitter node, the same thumb that used to pinch "
        "your cheeks when you were a kid. She licks her lips, hesitates, then looks "
        "at you with hunger disguised as gratitude."
    ))
    print()

    choice = prompt_choice(
        "How do you steady this moment before you willingly become less than a "
        "crumb?",
        {
            "reassure": "Reassure Katie with the speech you've rehearsed.",
            "joke": "Make a nervous joke about her not stepping on you.",
            "rush": "Tell her to hit the button before either of you can lose courage.",
        },
    )

    if choice == "joke":
        if death(
            "Your quip about her stepping on you triggers a distant look in Katie's "
            "eyes. She smiles in a way you've never seen and brings her bare heel "
            "down onto the belt while it still rests in your palms. The emitter "
            "fires. The belt shrinks, the air shrinks, you shrink. There is no "
            "transition—only the sudden crush of bone and metal as her full weight "
            "obliterates the spot where you once stood."
        ):
            return False

    if choice == "rush":
        if death(
            "You urge Katie to press the button now. She does, but the belt is still "
            "loosely buckled. When the world surges upward, the device slips. You "
            "plummet through the buckle, screaming up at a titanic silhouette that "
            "leans forward too late. The remote is fumbled; the next thing you see "
            "is the pad of her finger blotting out the light as it slams you against "
            "the floor like an ant beneath a closing book."
        ):
            return False

    print(wrap(
        "You swallow your terror and feed her the speech, each word a lifeline you "
        "throw out in the hope that she grabs the rope instead of you. She nods, "
        "breathing faster. The belt clicks closed around your waist, heavy and cold "
        "against your skin. Katie accepts the remote with trembling excitement."
    ))
    print()
    print(wrap(
        "You kneel on the oil-stained concrete, camera ready, and nod for her to "
        "try a modest reduction. The red digits blink 1.0 in tall block letters. "
        "Her thumbnail taps the keypad, wandering lower and lower until it stops at "
        "0.125. Her lips shape the fraction like a forbidden word. Then she presses "
        "“CONVERT.”"
    ))
    print()
    print(wrap(
        "Gravity vomits you downward. The garage swells, each particle of dust "
        "ballooning into a drifting boulder. By the time your ears stop ringing you "
        "are staring at a wall of painted toenails. Katie's right big toe twitches, "
        "and the ripple of muscle and skin above you may as well be a landslide."
    ))
    print()

    choice = prompt_choice(
        "The toe lifts. A shadow like storm clouds rolls your way. What do you do?",
        {
            "dash": "Dive toward the cold gleam of a dropped screw to use as cover.",
            "wave": "Plant your feet and wave frantically, trusting she will notice.",
            "freeze": "Freeze in place; maybe she will place her foot elsewhere.",
        },
    )

    if choice == "freeze":
        if death(
            "You trust in mercy. Mercy comes down as a colossal pad of flesh. The "
            "toe slams onto you, spreading you into a translucent stain that Katie "
            "absently smears across the concrete while searching for where you went."
        ):
            return False

    if choice == "wave":
        if death(
            "You throw your arms up, screaming her name. The motion draws her "
            "attention—downward, not to you, but to the remote she nearly drops. She "
            "stomps reflexively to keep her balance. The step lands directly over "
            "you, compressing your world into wet darkness before you can exhale."
        ):
            return False

    print(wrap(
        "You sprint across the cold floor as the toe smashes down behind you, the "
        "impact hurling you head over heels. Static fills your headset. Katie's "
        "confused muttering booms overhead as she pivots, her other foot descending "
        "like a guillotine. You roll under the overhang of a discarded toolbox just "
        "as her heel kisses the ground beside you."
    ))
    print()
    print(wrap(
        "Katie gasps. The sound gusts over you, warm and wine-sweet. Her fingers "
        "pinch the air until they snatch your torso. She lifts you through a gale of "
        "her own perfume, sets you on her palm, and staggers toward the house. "
        "Every step jostles your bones. When she finally deposits you on the varnish "
        "glow of her dining table, you collapse among crumbs the size of cinder "
        "blocks."
    ))
    print()
    print(wrap(
        "The remote blinks again. Katie's brow furrows as she turns the digits up to "
        "0.25. The world shrinks—just a little—until she can focus on you without "
        "squinting. 'Take a break,' she whispers, voice quavering with a blend of "
        "terror and exhilaration. Then she leaves you alone with the creaking wood, "
        "the humming refrigerator, and the distant thunder of her retreating steps."
    ))
    print()
    return True


def table_scene() -> bool:
    print(wrap(
        "The table is a planet of dark lacquer under your bare feet. A ring of "
        "condensation from Katie's forgotten glass towers nearby like a moat. The "
        "air tastes of lemon cleaner and the faint, sour ghost of wine. You clutch "
        "your camera because it is the only piece of normal-sized life left to you."
    ))
    print()

    choice = prompt_choice(
        "The silence presses in. You can't just wait. What do you investigate?",
        {
            "glass": "Approach the sweating wall of the water glass.",
            "remote": "Search for the remote she left on the placemat.",
            "edge": "Peer over the edge of the table to gauge the drop.",
        },
    )

    if choice == "edge":
        if death(
            "You inch toward the table's lip, drawn by the yawning drop. A vibration "
            "from Katie's distant footsteps shudders through the wood. It knocks you "
            "forward. You tumble, limbs pinwheeling, camera spinning away. The fall "
            "ends in a bone-shattering crunch on tile far below. By the time Katie "
            "returns, there is nothing left to rescue."
        ):
            return False

    if choice == "glass":
        if death(
            "You near the sweating cylinder. Cold droplets the size of watermelons "
            "burst against the wood, slickening the path. One bead rolls toward you, "
            "gathering speed. You try to back away, but the droplet engulfs you, "
            "crushing your chest against the table surface before spilling over the "
            "edge with you trapped inside, drowning in refracted daylight."
        ):
            return False

    print(wrap(
        "You stumble across the woven landscape of the placemat until you find the "
        "remote the size of a car hood. Its keypad glows with red numerals that "
        "mock your helplessness. The CONVERT button looms over you like an altar. "
        "Your hands shake as you consider climbing the device."
    ))
    print()

    choice = prompt_choice(
        "If you could reach the controls, maybe you could grow back. But the climb "
        "is treacherous.",
        {
            "climb": "Attempt to scale the remote toward the keypad.",
            "wait": "Back away and wait, hoping Katie returns calm.",
            "smash": "Try to pry open the battery hatch with your camera tripod.",
        },
    )

    if choice == "smash":
        if death(
            "You wedge the tripod into the battery seam and pry. The remote wobbles. "
            "Your leverage gives way and the device tips, landing squarely atop you. "
            "Plastic and circuitry flatten you with a brittle snap that echoes under "
            "the table like a gunshot."
        ):
            return False

    if choice == "climb":
        if death(
            "You scramble up the rubber ridges of the keypad. A sudden jolt ripples "
            "through the table as Katie laughs at something on the television in the "
            "next room. You lose your grip and slide down the face of the remote, "
            "slamming into the CONVERT key. The impact depresses it. The belt surges. "
            "You shrink beyond scale, past atoms, past awareness, dissolving into "
            "static."
        ):
            return False

    print(wrap(
        "You retreat from the remote and crouch beside a crumb, hugging your knees. "
        "Minutes stretch. Your heartbeat drums in your ears louder than the house. "
        "When the tremors return, they feel heavier, purposeful. Katie's silhouette "
        "blots out the chandelier as she glides back into the dining room. In one "
        "hand she carries the remote. In the other, a cupcake crowned with a spire "
        "of frosting taller than you are."
    ))
    print()
    return True


def cupcake_scene() -> bool:
    print(wrap(
        "Katie looms over the table, eyes shining with predatory delight. She sets "
        "the cupcake down beside you. The cake's crumb is a porous cliff face, the "
        "frosting a glacial field of sugary peaks. Her free hand reaches for you. "
        "Before you can dodge, two fingers clamp around your torso and lift you "
        "toward the confection."
    ))
    print()

    choice = prompt_choice(
        "She dangles you above the frosting, breath washing over you hot and sweet. "
        "How do you react?",
        {
            "plead": "Beg her to stop and remind her you're family.",
            "photograph": "Raise your camera and keep shooting to appease her.",
            "struggle": "Thrash against her grip and try to break free.",
        },
    )

    if choice == "struggle":
        if death(
            "You twist with all your strength. Katie's fingers tighten instinctively. "
            "Ribs crack like dry twigs. She gasps, releasing you—but from too high. "
            "You plummet past the cupcake and slam into the wooden table, spine "
            "shattering. Her scream is the last thunder you hear."
        ):
            return False

    print(wrap(
        "You force your arms to steady the camera, snapping shot after shot even as "
        "tears blur your viewfinder. Katie coos and lowers you. Frosting engulfs you "
        "up to the chest, cold and cloying. When she lets go, you sink to your knees, "
        "smeared in sugar and terror."
    ))
    print()

    choice = prompt_choice(
        "Katie's mouth opens above you, cavernous and dripping. The cupcake tilts as "
        "she prepares to taste her creation. You need to survive the next bite.",
        {
            "bury": "Dig into the frosting and hide beneath the surface.",
            "run": "Sprint across the icing toward the opposite edge.",
            "ride": "Stand tall and keep photographing, hoping obedience saves you.",
        },
    )

    if choice == "bury":
        if death(
            "You dive into the frosting, clawing downward. The sugary paste hardens "
            "around you like quicksand. Heat floods the tunnel as Katie's tongue "
            "sweeps overhead. Frosting liquefies, sliding you straight toward her "
            "gullet. Darkness, pressure, then the rhythmic crush of peristalsis as "
            "you are swallowed alive."
        ):
            return False

    if choice == "run":
        if death(
            "You sprint, but the frosting clings to your legs. Katie's lips descend, "
            "biting off the path ahead. The suction drags you forward. You tumble "
            "between her teeth, and the next bite she takes shears you in half."
        ):
            return False

    print(wrap(
        "You stand your ground, camera flashing as her tongue sweeps dangerously "
        "close. Each time she pauses, you show her the screen, letting the luminous "
        "images of her own mouth distract her hunger. She giggles, the sound a gale "
        "that nearly blows you over. Then, with a wicked grin, she extends her "
        "tongue and scoops you up whole."
    ))
    print()
    print(wrap(
        "The world becomes humid velvet. Her tongue presses you to the roof of her "
        "mouth. Saliva floods around you, tasting of vanilla and looming doom. You "
        "scream through the radio, a static-laced plea. Katie's lips part just long "
        "enough for you to shove the camera between them. The flash detonates, white "
        "light bursting inside her skull. She coughs, spitting you back onto the "
        "frosting in a spray of sugar and saliva."
    ))
    print()

    choice = prompt_choice(
        "Dizzied but alive, you must make one last decision before she tries again.",
        {
            "tongue": "Scramble onto her tongue willingly, hoping cooperation earns mercy.",
            "remote": "Leap from the cupcake toward the remote in her other hand.",
            "collapse": "Collapse and play possum, trusting pity to wake in her.",
        },
    )

    if choice == "collapse":
        if death(
            "You go limp, trusting the last scrap of humanity in Katie. She watches "
            "you, head cocked, then smiles sadly. 'Looks like my little snack is all "
            "tuckered out,' she murmurs before tilting the cupcake into her mouth. "
            "The world flips. You and the cake slide between her lips. Her teeth meet. "
            "Everything ends in a soggy crunch."
        ):
            return False

    if choice == "tongue":
        survived, prelude = mouth_gauntlet()
        if not survived:
            return False
        remote_escape(prelude)
        return True

    # Choosing the remote directly plunges Ian into one desperate bid for escape.
    remote_escape(None)
    return True


def mouth_gauntlet() -> tuple[bool, str]:
    """Handle the extended sequence of surviving inside Katie's mouth."""
    print(wrap(
        "You crawl toward her tongue, presenting yourself. Katie's grin stretches "
        "wide with greedy triumph. The moment your palms touch the velvet muscle, "
        "she rolls you inward. Darkness slams shut as her lips seal. The humid air "
        "pulses with her heartbeat, and saliva threads down like ropes trying to "
        "lasso your limbs."
    ))
    print()
    print(wrap(
        "The tongue arches, sluicing you toward the grinding silhouettes of her "
        "molars. Every breath tastes of frosting, wine, and looming digestion. "
        "When she chuckles, the sound reverberates through your ribs like drums "
        "played against your bones."
    ))
    print()

    choice = prompt_choice(
        "Her jaw opens just enough for a draft of air before clamping shut again. "
        "You are sliding toward a waiting row of teeth that glint with saliva. How "
        "do you fight the current?",
        {
            "brace": "Brace between two molars and pray they do not meet.",
            "wedge": "Jam your camera between the teeth to halt your slide.",
            "throat": "Dive toward her throat, hoping to reach the uvula and cling.",
        },
    )

    if choice == "brace":
        if death(
            "You spread your arms and legs, wedging yourself between two massive "
            "molars. They slam together instantly, pulping you into a bitter smear "
            "that Katie swallows before she even notices the crunch."
        ):
            return False, ""

    if choice == "throat":
        if death(
            "You scramble toward the dark pit of her throat. The next swallow drags "
            "you over the cliff. Muscular rings grip and squeeze, snapping bones like "
            "kindling while forcing you down into steaming black."
        ):
            return False, ""

    print(wrap(
        "You wrench your camera free from its strap and slam the metal frame into "
        "the gap between her back molars. The jaws crash down, but the camera holds, "
        "screeching against enamel. The impact flings you sideways into a pool of "
        "saliva, but at least you are not paste between her teeth—yet."
    ))
    print()
    print(wrap(
        "Katie groans, annoyed, and starts to toy with the obstruction. Her tongue "
        "presses you against her cheek, kneading with obscene patience. Each shove "
        "threatens to dislodge the camera. Somewhere beyond the fleshy walls, you "
        "hear her breathing quicken with frustration."
    ))
    print()

    choice = prompt_choice(
        "The wedge will not last. With every probing lick, the camera slips. You "
        "need a new plan before the molars meet. Where do you gamble your life?",
        {
            "cling": "Cling to her tongue and hope she relents.",
            "cheek": "Scramble up into the pouch of her cheek to trigger her gag reflex.",
            "spit": "Kick the camera loose yourself and ride the gush of saliva out.",
        },
    )

    if choice == "cling":
        if death(
            "You hug the tongue, digging in your nails. Katie hums with pleasure and "
            "tilts her head back. Gravity does the rest. Saliva floods past and you "
            "lose your grip, sliding straight into the crushing darkness of her "
            "throat."
        ):
            return False, ""

    if choice == "spit":
        if death(
            "You kick the camera free, trusting the surge to carry you out. Instead, "
            "the freed molars clap together. The impact hammers you flat against her "
            "tongue, breaking your spine before the next swallow drags you away."
        ):
            return False, ""

    print(wrap(
        "You scramble upward, fingers clawing into the slick wall of her cheek. The "
        "muscle flexes, trying to eject you, but you burrow higher, scraping the "
        "tender flesh with your boots. Katie gasps, chokes, and suddenly the world "
        "erupts into motion as she gags."
    ))
    print()
    print(wrap(
        "Her lips burst open. A torrent of saliva, frosting, and your own bruised "
        "body explodes outward. You slam into the table, skidding through a smear "
        "of icing while Katie coughs and clutches her throat. The camera clatters "
        "beside you, bent but still sparking with a weak ready light."
    ))
    print()

    prelude = (
        "You stagger upright, dripping and shaking. Katie is occupied hacking into "
        "her cupped palm, giving you seconds at most. The remote in her other hand "
        "hangs forgotten over the tabletop lip, its minus button glowing like "
        "salvation."
    )
    return True, prelude


def play_game() -> bool:
    if not intro_scene():
        return False
    if not table_scene():
        return False
    if not cupcake_scene():
        return False
    return True


def main() -> None:
    print(wrap(
        "Welcome to 'Tiny Photographer: The Descent'. You are Ian, a professional "
        "who shrinks for custom photoshoots. Tonight you volunteered to help your "
        "recently divorced Aunt Katie feel powerful. It may be the last mistake you "
        "ever make."))
    print()
    while True:
        if play_game():
            break
        print(wrap("Restarting..."))
        print()


if __name__ == "__main__":
    main()
