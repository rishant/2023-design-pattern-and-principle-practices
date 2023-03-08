package com.principle.solid.liskov_substitution;

/**
	Liskov Substitution Principle Achieved - using `Abstract` Class for Substitution
*/
//public class NoShape implements Shape{
public class NoShapeV2 extends AbstractShape{

	/** 
		Liskov Substitution Principle violation - It is Substitution able, Even if we don't override.
        We have to either provide Interface `Default` implementation /or/ `Abstract` Class for Substitution
	 */
//    @Override
//    public double area() {
//        throw new IllegalStateException("Cannot calculate area");
//    }
}
