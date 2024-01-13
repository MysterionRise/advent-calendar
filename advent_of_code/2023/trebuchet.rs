use std::fs;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = fs::read_to_string("trebuchet.txt")?;

    let mut sum = 0;
    for line in contents.lines() {
        let first_digit = line.chars().nth(0).unwrap();
        let last_digit = line.chars().last().unwrap();
        let calibration_value = first_digit.to_digit(10).unwrap() * 10 + last_digit.to_digit(10).unwrap();
        sum += calibration_value;
    }

    println!("Sum of calibration values: {}", sum);

    Ok(())
}
