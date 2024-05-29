$(document).ready(function() {
    // Fetch distinct state names and populate the State dropdown
    $.ajax({
        url: '/get_state',
        type: 'GET',
        success: function(response) {
            $('#State').empty();
            $('#State').append('<option value="">Select State</option>');
            $.each(response.states, function(key, value) {
                $('#State').append('<option value="' + value + '">' + value + '</option>');
            });
        },
        error: function(xhr, status, error) {
            console.error("Error fetching states:", error);
        }
    });

    // Function to fetch districts based on selected state
    function fetchDistricts(state) {
        if (state) {
            $.ajax({
                url: '/get_districts',
                type: 'GET',
                data: { state: state },
                success: function(response) {
                    $('#District').empty();
                    $('#District').append('<option value="">Select District</option>');
                    $.each(response.districts, function(key, value) {
                        $('#District').append('<option value="' + value + '">' + value + '</option>');
                    });
                },
                error: function(xhr, status, error) {
                    console.error("Error fetching districts:", error);
                }
            });
        } else {
            $('#District').empty();
            $('#District').append('<option value="">Select District</option>');
        }
    }

    // Event listener for State dropdown change
    $('#State').change(function() {
        var state = $(this).val();
        fetchDistricts(state);
    });

    // Fetch unique crop names and populate the Crop dropdown
    $.ajax({
        url: '/get_crops',
        type: 'GET',
        success: function(response) {
            $('#Crop').empty();
            $('#Crop').append('<option value="">Select Crop</option>');
            $.each(response.crops, function(key, value) {
                $('#Crop').append('<option value="' + value + '">' + value + '</option>');
            });
        },
        error: function(xhr, status, error) {
            console.error("Error fetching crops:", error);
        }
    });

     // Add this function to clear the predicted yield output
     function clearPredictedYield() {
        document.getElementById('predicted-yield').innerText = '';
    }

    // Call the clearPredictedYield function when the page loads
    window.onload = function() {
        clearPredictedYield();
    };
});
