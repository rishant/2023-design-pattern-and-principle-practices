package com.principle.solid.liskov_substitution;

import java.util.List;

public class AreaCalculator {

	public int sum(List<Shape> shapes) {

		int sum = 0;
		for(int i = 0; i < shapes.size(); i++) {
			Shape shape = shapes.get(i);
//			if(shape instanceof Square) {
//				sum += Math.pow(((Square)shape).getLength(), 2);
//			}
//			if(shape instanceof Circle) {
//				sum += Math.PI * Math.pow(((Circle)shape).getRadius(), 2);
//			}
			/** Open Closed Principle violation - It is Open for Modification but it should be Open for Extension */
//			if(shape instanceof Cube) {
//				sum += Math.PI * Math.pow(((Circle)shape).getRadius(), 2);
//			}
			
			/** Open Closed Principle Achieved - Using Interface */
			sum += shape.area();
		}
		return sum;
	}
	
	/** single responsibility principle violation */
//	public String json(List<Shape> shapes) {
//		return String.format("{sum: %s}", sum(shapes));
//	}
}
