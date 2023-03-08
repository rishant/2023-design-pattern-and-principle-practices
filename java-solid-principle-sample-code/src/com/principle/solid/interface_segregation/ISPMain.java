package com.principle.solid.interface_segregation;

import java.util.Arrays;
import java.util.List;

public class ISPMain {

	public static void main(String[] args) {
		System.out.println("Hello World");
		
		Cube cube = new Cube(10);
		Rectangle rectangle = new Rectangle(10,20);
		
		// Java 8
		List<Shape> shapes = Arrays.asList(cube, rectangle);

		for (Shape shape : shapes) {
			System.out.println(String.format("{shapes_sum: %s}", shape.area()));			
		}

		for (Shape shape : shapes) {
			if(shape instanceof ThreeDimensionalShape) {
				System.out.println(String.format("{shapes_volume: %s}", ((ThreeDimensionalShape)shape).volume()));				
			}
		}

	}
}
