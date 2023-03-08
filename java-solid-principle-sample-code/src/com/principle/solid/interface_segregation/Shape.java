package com.principle.solid.interface_segregation;

public interface Shape {
	double area();
	
	/** 
	 	Interface Segregation Principle Violation - If we added any New method into existing Interface then All 
        Implemented classes need to be modify. Instead-of that we can Create separate Interface with the specific 
        requirement and Implements only those classes which actually needed rather-then all need to modify. 
	 */
//	double volume();

}
