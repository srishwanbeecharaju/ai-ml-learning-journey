import numpy as np

class MatrixOperations:
    """
    Day 1: Building blocks for recommendation systems
    Learning: Linear algebra and NumPy fundamentals
    """
    
    def __init__(self):
        self.name = "Matrix Operations for RecSys"
        print("Day 1 Project: Matrix Operations initialized!")
    
    def create_user_item_matrix(self, n_users=100, n_items=50):
        """
        Simulate user-item interaction matrix
        """
        matrix = np.zeros((n_users, n_items))
        # Add some random ratings
        n_ratings = int(0.1 * n_users * n_items)
        
        for _ in range(n_ratings):
            user = np.random.randint(0, n_users)
            item = np.random.randint(0, n_items)
            rating = np.random.randint(1, 6)
            matrix[user, item] = rating
            
        return matrix
    
    def calculate_cosine_similarity(self, vector1, vector2):
        """
        Calculate cosine similarity between two vectors
        """
        dot_product = np.dot(vector1, vector2)
        norm1 = np.linalg.norm(vector1)
        norm2 = np.linalg.norm(vector2)
        
        if norm1 == 0 or norm2 == 0:
            return 0
        
        return dot_product / (norm1 * norm2)

if __name__ == "__main__":
    # Test the code
    matrix_ops = MatrixOperations()
    ratings = matrix_ops.create_user_item_matrix(10, 8)
    print("Created ratings matrix shape:", ratings.shape)
    print("Sample ratings:")
    print(ratings[:5, :5])
    
    # Test similarity
    user1 = ratings[0]
    user2 = ratings[1]
    similarity = matrix_ops.calculate_cosine_similarity(user1, user2)
    print(f"Similarity between user 0 and user 1: {similarity:.3f}")