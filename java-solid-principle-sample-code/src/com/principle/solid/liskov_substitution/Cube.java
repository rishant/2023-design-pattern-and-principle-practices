package com.principle.solid.liskov_substitution;

public class Cube implements Shape{

	private final int edge;

    public Cube(int edge) {
        this.edge = edge;
    }

    public int getEdge() {
        return edge;
    }

    @Override
    public double area() {
//    	formula A=6a2
        return 6 * Math.pow(getEdge(), 2);
    }
}
