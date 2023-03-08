package com.principle.solid.liskov_substitution;

public class NoShape implements Shape{

	/** 
		Liskov Substitution Principle violation - It is Substitution able, Even if we don't override.
        We have to either provide Interface `Default` implementation /or/ `Abstract` Class for Substitution
	 */
    @Override
    public double area() {
        throw new IllegalStateException("Cannot calculate area");
    }
}
