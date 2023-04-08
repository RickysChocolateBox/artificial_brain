import tensorflow as tf
from tensorflow.keras import layers, models

class VAE(tf.keras.Model):
    def __init__(self, input_dim, latent_dim, encoder_layers, decoder_layers, learning_rate=0.001):
        super(VAE, self).__init__()
        self.latent_dim = latent_dim
        self.encoder = self.build_encoder(input_dim, encoder_layers, latent_dim)
        self.decoder = self.build_decoder(input_dim, decoder_layers, latent_dim)
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

    def build_encoder(self, input_dim, encoder_layers, latent_dim):
        inputs = layers.Input(shape=input_dim)
        x = inputs
        for layer_size in encoder_layers:
            x = layers.Dense(layer_size, activation='relu')(x)
        z_mean = layers.Dense(latent_dim)(x)
        z_log_var = layers.Dense(latent_dim)(x)
        return models.Model(inputs, (z_mean, z_log_var), name='encoder')

    def build_decoder(self, input_dim, decoder_layers, latent_dim):
        inputs = layers.Input(shape=(latent_dim,))
        x = inputs
        for layer_size in decoder_layers:
            x = layers.Dense(layer_size, activation='relu')(x)
        outputs = layers.Dense(input_dim, activation='sigmoid')(x)
        return models.Model(inputs, outputs, name='decoder')

    def reparameterize(self, z_mean, z_log_var):
        eps = tf.random.normal(shape=z_mean.shape)
        return z_mean + tf.exp(0.5 * z_log_var) * eps

    def call(self, inputs, training=None, mask=None):
        z_mean, z_log_var = self.encoder(inputs)
        z = self.reparameterize(z_mean, z_log_var)
        return self.decoder(z)

    def train_step(self, data):
        with tf.GradientTape() as tape:
            z_mean, z_log_var = self.encoder(data)
            z = self.reparameterize(z_mean, z_log_var)
            x_recon = self.decoder(z)
            recon_loss = tf.reduce_mean(tf.keras.losses.binary_crossentropy(data, x_recon))
            kl_loss = -0.5 * tf.reduce_mean(1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var))
            total_loss = recon_loss + kl_loss
        grads = tape.gradient(total_loss, self.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.trainable_variables))
        return {'loss': total_loss, 'recon_loss': recon_loss, 'kl_loss': kl_loss}
