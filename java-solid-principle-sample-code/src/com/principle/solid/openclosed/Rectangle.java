package com.principle.solid.openclosed;

public class Rectangle implements Shape{

	private final int length;
	private final int width;

    public Rectangle(int length, int width) {
        this.length = length;
        this.width = width;
    }

    public int getLength() {
        return length;
    }
    
    public int getWidth() {
    	return width;
    }

    @Override
    public double area() {
//    	formula A=wl
        return length * width;
    }
}
