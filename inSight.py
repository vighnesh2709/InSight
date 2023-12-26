def evaluate_images(images):
    for reference_index in range(len(images)):
        reference_image = images[reference_index]
        clear_count = 0

        for current_image_index in range(len(images)):
            current_image = images[current_image_index]

            if current_image_index == reference_index:
                continue  # Skip comparing the image to itself

            clear = input(f"Is image {current_image_index + 1} clear compared to image {reference_index + 1}? (yes/no): ").lower()

            if clear == 'yes':
                clear_count += 1

        if clear_count == 0:
            print(f"The clearest image compared to image {reference_index + 1} is {reference_image}.")
            break  # Exit the loop as the clearest image is found

# Example usage
images = ["Image 1", "Image 2", "Image 3", "Image 4", "Image 5"]
evaluate_images(images)
