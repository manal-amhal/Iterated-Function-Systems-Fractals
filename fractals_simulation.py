import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. FLOCON DE VON KOCH
# ==========================================


def koch_curve(p1, p2, depth):
    """Génère récursivement les points de la courbe de Von Koch."""
    if depth == 0:
        return [p1, p2]

    p1 = np.array(p1)
    p2 = np.array(p2)

    # Calcul des 3 points intermédiaires
    s = p1 + (p2 - p1) / 3.0
    t = p1 + 2.0 * (p2 - p1) / 3.0

    # Point du sommet du triangle équilatéral (rotation de 60°)
    angle = np.pi / 3
    rotation_matrix = np.array(
        [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
    )
    u = s + np.dot(rotation_matrix, (t - s))é

    # Appels récursifs
    points = []
    points.extend(koch_curve(p1, s, depth - 1)[:-1])
    points.extend(koch_curve(s, u, depth - 1)[:-1])
    points.extend(koch_curve(u, t, depth - 1)[:-1])
    points.extend(koch_curve(t, p2, depth - 1))

    return points


def plot_koch_snowflake(depth=4):
    """Trace le flocon de Von Koch (3 courbes assemblées)."""
    # Sommets d'un triangle équilatéral initial
    p1 = [0, 0]
    p2 = [0.5, np.sin(np.pi / 3)]
    p3 = [1, 0]

    # Génération des 3 côtés
    side1 = koch_curve(p1, p2, depth)
    side2 = koch_curve(p2, p3, depth)
    side3 = koch_curve(p3, p1, depth)

    snowflake = np.array(side1 + side2 + side3)

    plt.figure(figsize=(6, 6))
    plt.plot(snowflake[:, 0], snowflake[:, 1], color='royalblue', lw=1.5)
    plt.axis('equal')
    plt.axis('off')
    plt.title(f'Flocon de Von Koch (Profondeur {depth})')
    plt.savefig('koch_snowflake.png', dpi=300, bbox_inches='tight')
    plt.show()


# ==========================================
# 2. TRIANGLE DE SIERPINSKI 
# ==========================================


def plot_sierpinski(n_points=50000):
    """Génère le triangle de Sierpinski avec l'algorithme du jeu du chaos."""
    # Sommets du triangle
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sin(np.pi / 3)]])

    points = np.zeros((n_points, 2))
    current_point = np.array([0.5, 0.2])

    for i in range(n_points):
        # Choisit un sommet au hasard
        random_vertex = vertices[np.random.randint(0, 3)]
        # Se déplace de moitié vers ce sommet
        current_point = (current_point + random_vertex) / 2.0
        points[i] = current_point

    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], s=0.1, color='crimson')
    plt.axis('equal')
    plt.axis('off')
    plt.title('Triangle de Sierpinski (IFS)')
    plt.savefig('sierpinski_triangle.png', dpi=300, bbox_inches='tight')
    plt.show()


# ==========================================
# 3. FOUGÈRE DE BARNSLEY -- Transformations Affines
# ==========================================


def plot_barnsley_fern(n_points=100000):
    """Génère la fougère de Barnsley à partir des 4 transformations affines."""
    x = np.zeros(n_points)
    y = np.zeros(n_points)

    for i in range(1, n_points):
        r = np.random.rand()

        if r < 0.01:
            # f1 : Tige
            x[i] = 0
            y[i] = 0.16 * y[i - 1]
        elif r < 0.86:
            # f2 : Feuillage supérieur
            x[i] = 0.85 * x[i - 1] + 0.04 * y[i - 1]
            y[i] = -0.04 * x[i - 1] + 0.85 * y[i - 1] + 1.6
        elif r < 0.93:
            # f3 : Branche gauche
            x[i] = 0.20 * x[i - 1] - 0.26 * y[i - 1]
            y[i] = 0.23 * x[i - 1] + 0.22 * y[i - 1] + 1.6
        else:
            # f4 : Branche droite
            x[i] = -0.15 * x[i - 1] + 0.28 * y[i - 1]
            y[i] = 0.26 * x[i - 1] + 0.24 * y[i - 1] + 0.44

    plt.figure(figsize=(6, 9))
    plt.scatter(x, y, s=0.1, color='forestgreen')
    plt.axis('equal')
    plt.axis('off')
    plt.title('Fougère de Barnsley (IFS)')
    plt.savefig('barnsley_fern.png', dpi=300, bbox_inches='tight')
    plt.show()


# ==========================================
# EXÉCUTION
# ==========================================
if __name__ == '__main__':
    print('Génération des fractales...')
    plot_koch_snowflake(depth=4)
    plot_sierpinski(n_points=50000)
    plot_barnsley_fern(n_points=100000)
    print('Terminé ! Les images ont été sauvegardées.')



    