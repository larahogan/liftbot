# liftbot

## Entering workout data:
    ?bench today 45x5 55x5 65x5
    ?deadlift today 65x5 85x5 105x5
    ?squat 11/30/2016 45x5 45x5 45x5

    ?bench goal 100x1
    ?bench goal 80x5
    ?deadlift goal 150x1

## Checking workout data

    ?1rm bench
        you don't have a 1rm saved yet!

*or*

    ?1rm bench
        your calculated 1rm based on your 12/1/2016 workout = **~75**

    ?1rm
        bench: 75 on XXXX
        squats: 100 on 12/1/2016

*This calculator is based on the formula derived by Boyd Epley in 1985, which is 1RM = weight x (1 + (reps / 30))*

*or, [https://en.wikipedia.org/wiki/One-repetition_maximum](Wikipedia)*

    ?last bench
        your last bench (12/1/2016): **45x5 55x5 65x5**

    ?all bench
        your bench workouts:
        12/1/2016 45x5 55x5 65x5
        11/30/2016 45x5 55x5 65x5
        11/28/2016 45x5 45x5 45x5 45x5 45x5

    ?last workout
        your last workout (12/2/2016):
        bench 45x5 55x5 65x5
        deadlift 65x5 85x5 105x5

    ?goal bench
        your bench goal: **100x1**, **80x5**

    ?bench today 45x5 65x5 75x5 85x5
        :tada:, you hit your bench goal of **80x5**!