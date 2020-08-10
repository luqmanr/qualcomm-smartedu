<template>
    <div style="height:100%; color: white;">

        <div v-for="question,index in questionAnswers" class="row">
            <span class="col-sm-12">{{question.question}}</span>
            <!-- <input v-for="answers in question.answers" :name="question.question" type="radio" :value="answers">{{answers}}</input> -->
            <div v-for="answers,ansIndex in question.answers" class="col-sm-12">
                
                <label>
                    <input type="radio" :id="answers" :name="index" @click="updateAnswer(index, ansIndex)">
                    <span>{{answers}}</span>
                </label>

            </div>
        </div>

        <button @click="emitAnswers">SUBMIT ANSWERS</button>

    </div>
</template>

<script>

import examQuestionsJSON from './exam_questions.json'

export default {
    data() {
        return {
            examQuestions: examQuestionsJSON,
            testAnswers: []
        }
    },
    computed: {
        questionAnswers() {
            return examQuestionsJSON.data.map(questions => {
                return questions
            })
        }
    },
    methods: {
        getQuestionsLength() {
            var index = examQuestionsJSON.data.length
            var i
            for (i in examQuestionsJSON.data) {
                // console.log(i)
                this.testAnswers.push(null)
            }
            // console.log(this.testAnswers)
        },
        updateAnswer(index, answers) {
            this.testAnswers[index] = answers;
            console.log(this.testAnswers)
        },
        emitAnswers() {
            this.$emit("emitAnswers", this.testAnswers)
        }
    },
    created() {
        this.getQuestionsLength()
    }
}
</script>

<style scoped>

</style>