package com.principle.solid.liskov_substitution;

import java.util.Arrays;
import java.util.List;

public class LSPMain {

	public static void main(String[] args) {
		System.out.println("Hello World");
		
		Circle circle = new Circle(10);
		Square square = new Square(10);
		Cube cube = new Cube(10);
		Rectangle rectangle = new Rectangle(10,20);
		
		/**
		 	Liskov Substitution Principle violation - It is Substitution able, Even if we don't override. 
		 */
//		NoShape noShape = new NoShape();
//		List<Shape> shapes = Arrays.asList(circle, square, cube, rectangle, noShape);
		
		/**
		 	Liskov Substitution Principle Achieved - using `Abstract` Class for Substitution
		 */
		NoShapeV2 noShapeV2 = new NoShapeV2();
		
		// Java 8
		List<Shape> shapes = Arrays.asList(circle, square, cube, rectangle, noShapeV2);
		
		// Java 11
//		List<Shape> shapes = List.of(circle, square);
		
		AreaCalculator areaCalculator = new AreaCalculator();
		int sum = areaCalculator.sum(shapes);
		System.out.println("sum = " + sum);
		
		// single responsibility principle violation
//		System.out.println(areaCalculator.json(shapes));
		
		// single responsibility principle Achieved.
		ShapePrinter shapePrinter = new ShapePrinter(areaCalculator);
		System.out.println(shapePrinter.json(shapes));
		System.out.println(shapePrinter.csv(shapes));
	}
}
