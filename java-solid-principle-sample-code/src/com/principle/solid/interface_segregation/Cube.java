package com.principle.solid.interface_segregation;

public class Cube implements Shape, ThreeDimensionalShape{

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

	@Override
	public double volume() {
//    	formula A=a3
		return Math.pow(getEdge(), 3);
	}
}
