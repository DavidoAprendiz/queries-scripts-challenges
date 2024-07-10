// iterators2.rs
//
// In this exercise, you'll learn some of the unique advantages that iterators
// can offer. Follow the steps to complete the exercise.
//
// Execute `rustlings hint iterators2` or use the `hint` watch subcommand for a
// hint.

pub fn capitalize_first(input: &str) -> String {
    let mut c = input.chars();
    match c.next() {
        None => String::new(),
        Some(first) => format!("{}{}", first.to_uppercase(), (input[1..].to_string())),
    }
}

pub fn capitalize_words_vector(words: &[&str]) -> Vec<String> {
    let mut my_vec = vec![];
    for word in words {
        my_vec.push(capitalize_first(word))
    }
    my_vec
}

pub fn capitalize_words_string(words: &[&str]) -> String {
    let mut my_str = String::from("");
    for word in words {
        my_str.push_str(&capitalize_first(word))
    }
    my_str
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_success() {
        assert_eq!(capitalize_first("hello"), "Hello");
    }

    #[test]
    fn test_empty() {
        assert_eq!(capitalize_first(""), "");
    }

    #[test]
    fn test_iterate_string_vec() {
        let words = vec!["hello", "world"];
        assert_eq!(capitalize_words_vector(&words), ["Hello", "World"]);
    }

    #[test]
    fn test_iterate_into_string() {
        let words = vec!["hello", " ", "world"];
        assert_eq!(capitalize_words_string(&words), "Hello World");
    }
}
