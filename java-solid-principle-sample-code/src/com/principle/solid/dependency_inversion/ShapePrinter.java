package com.principle.solid.dependency_inversion;

import java.util.List;

public class ShapePrinter {

	/**
	 	Dependency Inversion Violation - Taking Concreted Class Reference.
	
	private AreaCalculator areaCalculator = null;
	public ShapePrinter(AreaCalculator areaCalculator) {
        this.areaCalculator = areaCalculator;
    }
	*/
	
	/**
	 	Dependency Inversion Achieved - Instead of Concreted Class take a Interface Reference and Inject on-demand.
	 */
    private IAreaCalculator areaCalculator = null;

    public ShapePrinter(IAreaCalculator areaCalculator) {
        this.areaCalculator = areaCalculator;
    }

    public String json(List<Shape> shapes) {
        return String.format("{shapes_sum: %s}", areaCalculator.sum(shapes));
    }

    public String csv(List<Shape> shapes) {
        return String.format("shapes_sum,%s", areaCalculator.sum(shapes));
    }
}
