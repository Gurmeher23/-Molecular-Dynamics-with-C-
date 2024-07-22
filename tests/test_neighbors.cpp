#include "../include/Molecular-Dynamics/atoms.h"
#include "../include/Molecular-Dynamics/neighbors.h"
#include "../include/Molecular-Dynamics/xyz.h"

#include <gtest/gtest.h>

TEST(NeighborsTest, Test1) {
    Names_t names{{"H", "H", "H", "H"}};
    Positions_t positions(3, 4);
    positions << 0, 1, 0, 0,
                 0, 0, 1, -1,
                 0, 0, 0, 0;

    Atoms atoms(names, positions);
    NeighborList neighbor_list(1.5);
    auto &[seed, neighbors]{neighbor_list.update(atoms)};

    // All atoms except 3 and 4 are neighbors of each other
    EXPECT_EQ(neighbor_list.nb_neighbors(), 10);

    EXPECT_EQ(neighbor_list.nb_neighbors(0), 3);
    EXPECT_EQ(neighbor_list.nb_neighbors(1), 3);
    EXPECT_EQ(neighbor_list.nb_neighbors(2), 2);
    EXPECT_EQ(neighbor_list.nb_neighbors(3), 2);

    EXPECT_TRUE((neighbors(Eigen::seq(seed(0), seed(1) - 1)) == Eigen::Array3i{3, 1, 2}).all());
    EXPECT_TRUE((neighbors(Eigen::seq(seed(1), seed(2) - 1)) == Eigen::Array3i{3, 0, 2}).all());
    EXPECT_TRUE((neighbors(Eigen::seq(seed(2), seed(3) - 1)) == Eigen::Array2i{0, 1}).all());
    EXPECT_TRUE((neighbors(Eigen::seq(seed(3), seed(4) - 1)) == Eigen::Array2i{0, 1}).all());
}


TEST(NeighborsTest, FirstAtomHasNoNeighbor) {
    Names_t names{{"H", "H", "H", "H"}};
    Positions_t positions(3, 4);
    positions << 0, 7, 0, 0,
                 0, 0, 7, 6,
                 0, 0, 0, 0;

    Atoms atoms(names, positions);
    NeighborList neighbor_list(5.0);
    neighbor_list.update(atoms);

    auto &[seed, neighbors]{neighbor_list.update(atoms)};

    EXPECT_EQ(neighbor_list.nb_neighbors(), 2);

    EXPECT_EQ(neighbor_list.nb_neighbors(0), 0);
    EXPECT_EQ(neighbor_list.nb_neighbors(1), 0);
    EXPECT_EQ(neighbor_list.nb_neighbors(2), 1);
    EXPECT_EQ(neighbor_list.nb_neighbors(3), 1);

    EXPECT_TRUE((seed == Eigen::Array<int, 5, 1>{0, 0, 0, 1, 2}).all());
    EXPECT_TRUE((neighbors == Eigen::Array<int, 2, 1>{3, 2}).all());

    for (auto[i, j]: neighbor_list) {
        if (i == 2) EXPECT_EQ(j, 3);
        if (i == 3) EXPECT_EQ(j, 2);
    }
}


TEST(NeighborsTest, LastAtomHasNoNeighbor) {
    Names_t names{{"H", "H", "H"}};
    Positions_t positions(3, 3);
    positions << 0, 0, 0,
                 7, 6, 0,
                 0, 0, 0;

    Atoms atoms(names, positions);
    NeighborList neighbor_list(5.0);
    neighbor_list.update(atoms);

    auto &[seed, neighbors]{neighbor_list.update(atoms)};

    EXPECT_EQ(neighbor_list.nb_neighbors(), 2);

    EXPECT_EQ(neighbor_list.nb_neighbors(0), 1);
    EXPECT_EQ(neighbor_list.nb_neighbors(1), 1);
    EXPECT_EQ(neighbor_list.nb_neighbors(2), 0);

    EXPECT_TRUE((seed == Eigen::Array<int, 4, 1>{0, 1, 2, 2}).all());
    EXPECT_TRUE((neighbors == Eigen::Array<int, 2, 1>{1, 0}).all());

    for (auto[i, j]: neighbor_list) {
        if (i == 0) EXPECT_EQ(j, 1);
        if (i == 1) EXPECT_EQ(j, 0);
    }
}


TEST(NeighborsTest, AtomsHaveNoNeighbors) {
    Names_t names{{"H", "H", "H", "H"}};
    Positions_t positions(3, 4);
    positions << 0, 7, 0, 0,
                 0, 0, 7, 6,
                 0, 0, 0, 0;

    Atoms atoms(names, positions);
    NeighborList neighbor_list(0.5);  // this is below the smallest distance
    neighbor_list.update(atoms);

    auto &[seed, neighbors]{neighbor_list.update(atoms)};

    EXPECT_EQ(neighbor_list.nb_neighbors(), 0);

    EXPECT_EQ(neighbor_list.nb_neighbors(0), 0);
    EXPECT_EQ(neighbor_list.nb_neighbors(1), 0);
    EXPECT_EQ(neighbor_list.nb_neighbors(2), 0);
    EXPECT_EQ(neighbor_list.nb_neighbors(3), 0);

    int n{0};
    for (auto[i, j]: neighbor_list) {
        n++;
    }
    EXPECT_EQ(n, 0);
}


