package com.principle.solid.dependency_inversion;

import java.util.Arrays;
import java.util.List;

public class DIPMain {

	public static void main(String[] args) {
		System.out.println("Hello World");
		
		Square square = new Square(10);
		
		List<Shape> shapes = Arrays.asList(square);
		
		IAreaCalculator areaCalculator = new AreaCalculator();		
		/**	Dependency Inversion Achieved - Instead of Concreted Class take a Interface Reference and Inject on-demand. */
		ShapePrinter shapePrinter = new ShapePrinter(areaCalculator);
		System.out.println(shapePrinter.json(shapes));
		System.out.println(shapePrinter.csv(shapes));
		
		areaCalculator = new AreaCalculatorV2();
		/**	Dependency Inversion Achieved - Instead of Concreted Class take a Interface Reference and Inject on-demand. */
		shapePrinter = new ShapePrinter(areaCalculator);
		System.out.println(shapePrinter.json(shapes));
		System.out.println(shapePrinter.csv(shapes));
	}
}
