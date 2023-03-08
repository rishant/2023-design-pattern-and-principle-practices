package com.principle.solid.openclosed;

import java.util.List;

public class ShapePrinter {

    private AreaCalculator areaCalculator = null;

    public ShapePrinter(AreaCalculator areaCalculator) {
        this.areaCalculator = areaCalculator;
    }

    public String json(List<Shape> shapes) {
        return String.format("{shapes_sum: %s}", areaCalculator.sum(shapes));
    }

    public String csv(List<Shape> shapes) {
        return String.format("shapes_sum,%s", areaCalculator.sum(shapes));
    }
}
