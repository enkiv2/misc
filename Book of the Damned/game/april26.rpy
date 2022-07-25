# At 80% of the way through the runtime, this is the "all is lost" moment
# if she survives, then we have three days of planning before she can get the 'true end' april 30 - may 1
# if she doesn't survive then this is game over, so put a false failure at the new midpoint (april 5) and a false success at the new 80% mark (april 18)
label drugged_scene:
    comment "Misato is summoned to Corto's penthouse. She is offered tea, and drinks it, as he monologues at her. She wonders why she's here."
    comment "She begins to hallucinate: her vision gets slightly fuzzy, she begins to see tiny figures marching along the edge of the teacup,  it morphs into a desert landscape, etc."
    if cat_affinity >= 75:
        comment "If cat affinity is high enough, this transitions to a Louis Wain style of cats marching in, and Misato wakes up downstairs. She later discovers Corto has been mauled."
        $ achievement.grant("Moja sestra? Moja sestra.")
    else:
        comment "Otherwise, there is a warped & delirious perception of Misato's violation and murder"
        comment "initially, with increasingly dark imagery:"
        comment "the desert landscape becomes a geometric garden (like Last Year At Marienbad), but the shrubs become wheels (fading into the final shot of Ken Russel's The Devils)"
        comment "then, fish and bubbles and a blur/haze overlay this: it is underwater"
        comment "after this, we get description --"
        comment "(extremely vague: shapes pressing on her, a warm feeling lapping at her neck as she feels like she's floating, followed by the game announcing her death)."
        comment "death is followed by tv static animation"
        $ achievement.grant("Heaviside layer")
        call badEnd
        return
