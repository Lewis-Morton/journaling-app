import { ScrollView, View, Text, StyleSheet } from "react-native";

export default function Chat() {
    return(
        <ScrollView style={{ flex: 1, backgroundColor: 'white' }}>
            <View style={{ padding: 20 }}>
                <Text >Chat</Text>
            </View>
        </ScrollView>
    );
}