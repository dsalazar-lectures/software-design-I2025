package lab3.adapter;

import lab3.adapter.adapters.SquarePegAdapter;
import lab3.adapter.round.RoundHole;
import lab3.adapter.round.RoundPeg;
import lab3.adapter.square.SquarePeg;

public class Demo {
    public static void main(String[] args) {
        RoundHole hole = new RoundHole(5);
        RoundPeg roundPeg = new RoundPeg(5);
        System.out.println(hole.fits(roundPeg)
                ? "Round peg r5 fits round hole r5."
                : "Round peg r5 does not fit round hole r5.");

        SquarePeg smallSquarePeg = new SquarePeg(2);
        SquarePeg largeSquarePeg = new SquarePeg(20);

        // This will not compile because SquarePeg is not compatible with RoundHole.
        // Try commenting/uncommenting the line below to simulate the error.
        /*
        System.out.println(hole.fits(smallSquarePeg)
                ? "Square peg w2 fits round hole r5."
                : "Square peg w2 does not fit round hole r5.");
        */

        // Now using the Adapter to make SquarePeg compatible
        SquarePegAdapter smallAdapter = new SquarePegAdapter(smallSquarePeg);
        SquarePegAdapter largeAdapter = new SquarePegAdapter(largeSquarePeg);

        System.out.println(hole.fits(smallAdapter)
                ? "Square peg w2 fits round hole r5."
                : "Square peg w2 does not fit round hole r5.");

        System.out.println(hole.fits(largeAdapter)
                ? "Square peg w20 fits round hole r5."
                : "Square peg w20 does not fit round hole r5."); 
        
    }
                      
}
