<article class="day-desc"><h2>--- Day 13: Knights of the Dinner Table ---</h2><p>In years past, the holiday feast with your family hasn't gone so well.  Not everyone gets along!  This year, you resolve, will be different.  You're going to find the <em>optimal seating arrangement</em> and avoid all those awkward conversations.</p>
<p>You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person.  You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.</p>
<p>For example, suppose you have only four attendees planned, and you <span title="Finding a method to calculate happiness units is left as an exercise for the reader.">calculate</span> their potential happiness as follows:</p>
<pre><code>Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
</code></pre>
<p>Then, if you seat Alice next to David, Alice would lose <code>2</code> happiness units (because David talks so much), but David would gain <code>46</code> happiness units (because Alice is such a good listener), for a total change of <code>44</code>.</p>
<p>If you continue around the table, you could then seat Bob next to Alice (Bob gains <code>83</code>, Alice gains <code>54</code>).  Finally, seat Carol, who sits next to Bob (Carol gains <code>60</code>, Bob loses <code>7</code>) and David (Carol gains <code>55</code>, David gains <code>41</code>).  The arrangement looks like this:</p>
<pre><code>     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
</code></pre>
<p>After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of <code>330</code>.</p>
<p>What is the <em>total change in happiness</em> for the optimal seating arrangement of the actual guest list?</p>
</article>
<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>In all the commotion, you realize that you forgot to seat yourself.  At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to.  You assume everyone else would be just as ambivalent about sitting next to you, too.</p>
<p>So, add yourself to the list, and give all happiness relationships that involve you a score of <code>0</code>.</p>
<p>What is the <em>total change in happiness</em> for the optimal seating arrangement that actually includes yourself?</p>
</article>
