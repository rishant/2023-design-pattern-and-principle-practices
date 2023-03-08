package com.principle.solid.single_responsibility;

import java.util.List;

public class AreaCalculator {

	public int sum(List<Shape> shapes) {

		int sum = 0;
		for(int i = 0; i < shapes.size(); i++) {
			Shape shape = shapes.get(i);
			if(shape instanceof Square) {
				sum += Math.pow(((Square)shape).getLength(), 2);
			}
			if(shape instanceof Circle) {
				sum += Math.PI * Math.pow(((Circle)shape).getRadius(), 2);
			}
		}
		return sum;
	}
	
	// single responsibility principle violation
//	public String json(List<Shape> shapes) {
//		return String.format("{sum: %s}", sum(shapes));
//	}
}
